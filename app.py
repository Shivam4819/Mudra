from flask import Flask, jsonify,request
from MFHouse import MF
from StockList import StockList
from TopSectors import Sector
from TopSectorCompany import TopCompany
app = Flask(__name__)


@app.route("/fund")
def mf_house():
  return MF.fund_house_data_set()

@app.route("/stock")
def stock_list():
  return StockList.get_stock_from_csv()

@app.route("/sector")
def sector():
  return Sector.top_sector()

@app.route("/tops")
def company():
  return TopCompany.get_top_company()

  