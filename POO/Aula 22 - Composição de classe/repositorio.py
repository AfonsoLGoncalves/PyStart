from sql_actions.insert import Insert
from sql_actions.select import Select

# Composição de classe / Facade desing Pattern
# Permite sem precisar de uma herança
class Repositorio:

    def __init__(self) -> None:
        self.__insert = Insert()
        self.__select = Select()

    def select_by_id(self):
        self.__select.select_one()

    def select_by_group(self):
        self.__select.select_many()