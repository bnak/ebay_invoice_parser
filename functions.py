import csv


class Invoice:
    def __init__(self, start_time, end_time, line_items):
        # self.invoice_number = invoice_number
        self.start_time = start_time
        self.end_time = end_time
        self.line_items = line_items

    def display_contents(self):
        print("Start time: " + self.start_time)
        print("End time: " + self.end_time)
        print("Number of line items: " + str(len(self.line_items)))


class Item:
    def __init__(self):
        self.date_sold = ""
        self.title = ""
        self.item_id = ""
        self.fees = []

    def display_items(self):
        print ("Date sold: " + self.date_sold)
        print ("Title: " + self.title)
        print ("Item id: " + self.item_id)
        for item in self.fees:
            item.display_fee()


class Fee:
    def __init__(self, fee_type, amount):
        self.fee_type = fee_type
        self.amount = amount

    def display_fee(self):
        print("Fee type: " + self.fee_type)
        print("Fee amount: " + self.amount)


def read_csv(csv_path):
    with open(csv_path, 'rb') as csvfile:
        data = [row for row in csv.reader(csvfile.read().splitlines())]
    return data


def read_invoice(csv_path):
    file_contents = read_csv(csv_path)
    start_time = file_contents[2][0].split("to")[0][12:]
    end_time = file_contents[2][0].split("to")[1]
    line_items = file_contents[5:]
    invoice = Invoice(start_time, end_time, line_items)

    invoice.display_contents()

    return invoice


def parse_line_items(invoice):
    sold_items = {}
    for item in invoice.line_items:
        date_sold = item[0]
        title = item[1]
        item_id = item[2]
        fee_type = item[3]
        fee_amount = item[4]
        fee = Fee(fee_type, fee_amount)
        if sold_items.get(item_id):
            item = sold_items.get(item_id)
            item.fees.append(fee)
            sold_items[item_id] = item
        else:
            item = Item()
            setattr(item, 'date_sold', date_sold)
            setattr(item, 'title', title)
            setattr(item, 'item_id', item_id)
            setattr(item, 'fees', [fee])
            sold_items[item_id] = item

    return sold_items


def write_row_to_csv(output_file, array):
    f = open(output_file, 'a')
    writer = csv.writer(f)
    writer.writerow(array)
    f.close()
