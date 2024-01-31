import pandas as pd
from fpdf import FPDF

class ProductViewer:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def display_products(self):
        print("Available Products:")
        print(self.df)

    def select_product(self):
        while True:
            try:
                item_id = int(input("Enter the ID of the item you want to purchase: "))
                selected_product = self.df[self.df['id'] == item_id].squeeze()
                return selected_product
            except ValueError:
                print("Invalid input. Please enter a valid item ID.")

class ReceiptGenerator:
    def __init__(self, output_file):
        self.output_file = output_file

    def generate_receipt(self, receipt_data):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for key, value in receipt_data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

        pdf.output(self.output_file)

if __name__ == "__main__":
    csv_file = "articles.csv"
    viewer = ProductViewer(csv_file)
    viewer.display_products()
    selected_item = viewer.select_product()

    receipt_data = {
        "Receipt Number": selected_item['id'],
        "Product Name": selected_item['name'],
        "Price": selected_item['price']
    }

    receipt_output_file = f"receipt_{selected_item['id']}.pdf"
    receipt_generator = ReceiptGenerator(receipt_output_file)
    receipt_generator.generate_receipt(receipt_data)

    print(f"Receipt generated: {receipt_output_file}")