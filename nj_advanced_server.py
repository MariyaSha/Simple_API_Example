from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# create data model
class Product(BaseModel):
	units: str
	qty: int

# create NJ warehouse catalog
catalog = {
	"tomatoes": Product(
		units="boxes", 
		qty=1000
		),
	"wine": Product(
		units="bottles", 
		qty=500
		)
}

# create API server
app = FastAPI(title = "New Jersey API Server")

# set up an endpoint for all catalog products
@app.get("/warehouse/{product}")
async def load_truck(product, order_qty):
    """
    deduct ordered product quantity from the catalog,
    updating the inventory.
    """
    # the available product quantity
    available = catalog[product].qty

    # if order quantity is greater than the quantity at hand
    if int(order_qty) > int(available):
        # don't process the order - raise an exception
        raise HTTPException(
            status_code=400,
            detail=f"Sorry, only {available} units are available, please try again…"
        )
    # otherwise - process order, and subtract order quantity from the inventory
    catalog[product].qty -= int(order_qty)

    # produce shipping confirmation
    return {
        "product": product,
        "order_qty": order_qty,
        "units": catalog[product].units,
        "remaining_qty": catalog[product].qty
    }
