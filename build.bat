@echo off
python -m PyQt5.uic.pyuic -x Dashboard.ui -o gui/Dashboard.py
python -m PyQt5.uic.pyuic -x MiniCalc.ui -o gui/MiniCalc.py
python -m PyQt5.uic.pyuic -x TradeRuns.ui -o gui/TradeRuns.py
python -m PyQt5.uic.pyuic -x TradeCard.ui -o gui/TradeCard.py
python -m PyQt5.uic.pyuic -x PriceSheet.ui -o gui/PriceSheet.py
python -m PyQt5.uic.pyuic -x InfoCard.ui -o gui/InfoCard.py
python -m PyQt5.uic.pyuic -x ShipHangar.ui -o gui/ShipHangar.py
python -m PyQt5.uic.pyuic -x CompareTool.ui -o gui/CompareTool.py
python -m PyQt5.uic.pyuic -x Settings.ui -o gui/Settings.py
python -m PyQt5.uic.pyuic -x LocationSelector.ui -o gui/LocationSelector.py
python -m PyQt5.uic.pyuic -x Admin.ui -o gui/Admin.py
