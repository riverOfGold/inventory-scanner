import ui
import Barcode_Scanner as bs

class homeScreen(ui.View):
  def __init__(self, *args, **kwargs):
    self.present('sheet', hide_title_bar=True)
    
  def did_load(self):
    # this gets called once the UI file has fully loaded
    self.name_lbl = ui.Label(self, text="Name")
    self.count_lbl = ui.Label(self, text="Count")
    self.location_lbl = ui.Label(self, text="Location")
    self.supplier_lbl = ui.Label(self, text="Supplier")

    self.scan_btn = ui.Button(self, title="Scan")
    self.save_btn = ui.Button(self, title="Save")

    self.scan_btn.action = lambda a: self.read_from_api(self.scan_btn, self.barcode_text)
    self.save_btn.action = lambda a: self.write_to_api(self.scan_btn, self.barcode_text)
  
  def read_from_api(self, sender, target):
    pass

  def write_to_api(self, sender, target):
    pass

if __name__ == "__main__":
  test = homeScreen()
