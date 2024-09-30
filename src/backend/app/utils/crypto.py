from app.models.model import Model

Crypto = ["SOL-USD", "BTC-USD", "ETH-USD", "LTC-USD", "XRP-USD", "ADA-USD", "DOT-USD"]

Models_Crypto = [Model(model_name=crypto, gridfs_path="") for crypto in Crypto]
