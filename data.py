import Nessie

class RV:
    def __init__(self):
        self.spent = [[ 0 for i in range(31)] for j in range(12) ]
        self.earned = [[ 0 for i in range(31)] for j in range(12) ]
        self.saved = [[ 0 for i in range(31)] for j in range(12) ]
        self.gave = [[ 0 for i in range(31)] for j in range(12) ]


def get_data(ID):
    rv = RV()
    customer = Nessie.Customer(ID)
    accounts = Nessie.Account.get_by_custID(ID)
    transfers = Nessie.Transfer.get_by_custID(ID)

    try:
        for transfer in transfers:
            d = [int(m) for m in transfer.transaction_date.split("/")]
            if transfer.payer_id == ID:
                rv.spent[d[1]][d[2]] += transfer.amount
            else:
                rv.earned[d[1]][d[2]] += transfer.amount
    except:
        return None

    return rv





