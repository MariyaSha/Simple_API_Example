from fastapi import FastAPI, HTTPException

catalog = {
    "tomatoes":       {
        "unit": "boxes",  
        "qty": 1000
    },
    "wine": {
        "unit": "bottles", 
        "qty": 500
    },
    "corn": {
        "unit": "bags", 
        "qty": 5
    },
    "cranberries": {
        "unit": "boxes", 
        "qty": 5000
    }
}

app = FastAPI(title = "New Jersey API")

@app.get("/warehouse/{item}")
async def load_truck(item, order_qty):
    available = catalog[item]["qty"]

    if int(order_qty) > int(available):
        print("raising exception...")
        raise HTTPException(
            status_code=400,
            detail=f"Sorry, only {available} units are available, please try again…"
        )
    
    catalog[item]["qty"] -= int(order_qty)

    return {
        "item": item,
        "order_qty": order_qty, 
        "unit": catalog[item]["unit"],
        "remaining_qty": catalog[item]["qty"]
    }
