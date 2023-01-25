def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        for data in data_list:
            datafile.write(','.join(data))

def print_bus():
    return read_data_from_file('bus.txt')

def add_bus():
    name = input("Введите название автобуса: ")
    number = input("Введите госномер автобуса: ")
    return save_data_to_file('bus.txt', '\n' + name + ", " + number)

def print_driver():
    return read_data_from_file('driver.txt')

def add_driver():
    driver_id = input("Введите ID водителя: ")
    lastname = input("Введите фамилию водителя: ")
    return save_data_to_file('driver.txt', '\n' + driver_id + ", " + lastname)
    
def print_route():
    routes = read_data_from_file('route.txt')
    buses = read_data_from_file('bus.txt')
    drivers = read_data_from_file('driver.txt')
    print('|Route  |   №| Driver |    Bus    |')
    print('-'*37)
    for r_name,r_number, r_bus, r_driver in routes:
        bus_number = get_item_by_id(r_bus, buses)
        driver_name = get_item_by_id(r_driver, drivers)
        print('|{:>7}|{:>4}|{:>9}|{:>9}|'.format(r_name,r_number,driver_name, r_bus))    


def get_item_by_id(id, records):
    for id_record, item_record in records:
        if id == id_record:
            return item_record
            break
    return id      

def add_route():
    route_id = input("Введите ID маршрута: ")
    route_number = input("Введите номер маршрута: ")
    bus_id = input("Введите ID автобуса: ")
    driver_id = input("Введите ID водителя: ")
    return save_data_to_file('route.txt', '\n' + route_id + ", " + route_number + ", " + bus_id + ", " + driver_id)