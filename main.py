from fastapi import FastAPI, APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
import uvicorn
import os

from analysis import (
    generate_current_ratio,
    generate_quick_ratio,
    generate_proprietary_ratio,
    generate_inventory_ratio,
    generate_net_profit_ratio,
    generate_gross_profit_ratio,
    generate_fixed_asset_turnover_ratio,
    future_prediction_current_ratio,
    future_prediction_net_profit_ratio,
)


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
router = APIRouter()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

ratio_function_map = {
    "Current Ratio": generate_current_ratio,
    "Quick Ratio": generate_quick_ratio,
    "Proprietory Ratio": generate_proprietary_ratio,
    "Inventory Ratio": generate_inventory_ratio,
    "Fixed Asset Turnover Ratio": generate_fixed_asset_turnover_ratio,
    "Gross Profit Ratio": generate_gross_profit_ratio,
    "Net Profit Ratio": generate_net_profit_ratio,
}
available_ratios = list(ratio_function_map.keys())

prediction_function_map = {
    "Current Ratio": future_prediction_current_ratio,
    "Net Profit Ratio": future_prediction_net_profit_ratio,
}

available_predictions = list(prediction_function_map.keys())


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "plot": None,
            "ratios": available_ratios,
            "predictions": available_predictions,
        },
    )


@app.get("/health")
def read_root():
    return {"status": "healthy"}


@app.post("/", response_class=HTMLResponse)
async def handle_form(
    request: Request,
    form_type: Optional[str] = Form(None),
    ratio_type: Optional[str] = Form(None),
    prediction_type: Optional[str] = Form(None),
):

    context = {
        "request": request,
        "ratios": list(ratio_function_map.keys()),
        "predictions": list(prediction_function_map.keys()),
        "plot": None,
        "prediction": None,
        "selected_ratio": ratio_type,
        "selected_prediction": prediction_type,
    }

    try:
        if form_type == "ratio" and ratio_type:
            func = ratio_function_map.get(ratio_type)
            if func:
                context["plot"] = func()
        elif form_type == "prediction" and prediction_type:
            func = prediction_function_map.get(prediction_type)
            if func:
                context["prediction"] = func()
    except Exception as e:
        context["error"] = str(e)
    return templates.TemplateResponse("index.html", context)


is_dev = os.getenv("ENVIRONMENT", "development") == "development"


# Optional: run function for launching via `python main.py`
def run():
    uvicorn.run(
        "main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=is_dev
    )


# Ensure it only runs when executed directly
if __name__ == "__main__":
    run()
