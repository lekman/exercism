def exchange_money(budget:float, exchange_rate:float) -> float:
    """Gets the exchange value.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget:float, exchanging_value:int) -> float:
    """Gets the remainder of the budget after an exchange has been made.

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return  budget - exchanging_value


def get_value_of_bills(denomination:int, number_of_bills:int) -> int:
    """Gets the total value of bills for a set denomination.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget:float, denomination) -> int:
    """Gets the whole number of bills that can be returned, at value of denomination, from budget.
    
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """ 
    return budget // denomination

def rate_with_commission(exchange_rate:float, spread:int) -> float:
    """Returns the exchange rate including the commission cost.
    
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :return: float - exchange rate including commission cost.
    """
    return exchange_rate + (exchange_rate * spread / 100)

def exchangeable_value(budget:float, exchange_rate:float, spread:int, denomination:int) -> int:
    """Returns the whole denomination value.
    
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    return get_number_of_bills(
        exchange_money(
            budget, 
            rate_with_commission(
                exchange_rate, 
                spread)
        ), 
        denomination) * denomination


def non_exchangeable_value(budget:float, exchange_rate:float, spread:int, denomination:int) -> int:
    """Calculates the non-exchangeable value.

    The remainder value is calculated by deducting the correctly exchanged, whole denomination value from the total budget.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    return int(
        exchange_money(
            budget, 
            rate_with_commission(
                exchange_rate, spread)) - 
        exchangeable_value(
            budget, 
            exchange_rate, 
            spread, 
            denomination))
