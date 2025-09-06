from fastapi import FastAPI

catalog = {
	"tomatoes": {
		"units": "boxes",
		"qty": 1000
	},
	"wine": {
		"units": "bottles",
		"qty": 500
	}
}

app = FastAPI( title = "New Jersey API Server")

@app.get("/warehouse/{product}")
async def load_truck(product, order_qty):

	available = catalog[product]["qty"]

	if int(order_qty) > int(available):
		from fastapi import HTTPException
		raise HTTPException(
		    status_code=400,
		    detail=f"Sorry, only {available} units are available, please try again…"
		)

	catalog[product]["qty"] -= int(order_qty)

	return {
		"product": product,
		"order_qty": order_qty,
		"units": catalog[product]["units"],
		"remaining_qty": catalog[product]["qty"]
	}

