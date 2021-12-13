from typing import Any
from HashMap.Iloc import Iloc


class ModifiedDict(dict):

    def __init__(self, *args, **kw) -> None:
        self.__dict_array = []
        self.iloc = Iloc(self.__dict_array)
        super(ModifiedDict, self).__init__(*args, **kw)


    def __getitem__(self, __k) -> Any:
        return super().__getitem__(__k)


    def update(self, item: dict) -> None:
        key, value = list(item.items())[0][0], list(item.items())[0][1]
        self.__update_dict_array(key, value)
        return super().update(item)


    def __update_dict_array(self, __k, v) -> None:
        index_to_paste = -1
        key_was_found = False
        for index, dict_obj in enumerate(self.__dict_array):
            if __k < dict_obj[index][0]:
                index_to_paste = index
                break
            elif __k == dict_obj[index][0]:
                key_was_found = True 
                index_to_paste = index
                break

        if not key_was_found:
            if index_to_paste == 0:
                self.__dict_array = [(__k, v)] + self.__dict_array
                # костыль, лист меняет ссылку при переопредлении первого элемента
                self.iloc = Iloc(self.__dict_array)
            elif index_to_paste > 0:
                self.__dict_array = self.__dict_array[:index_to_paste - 1] + [(__k, v)] + self.__dict_array[index_to_paste -1:]
            else:
                self.__dict_array.append((__k, v))
        else: 
            self.__dict_array[index_to_paste] = (__k, v)


    def __setitem__(self, __k, v) -> None:
        self.__update_dict_array(__k, v)
        return super().__setitem__(__k, v)


    def __delitem__(self, __k) -> None:
        for index, item in enumerate(self.__dict_array):
            if __k == item[0]:
                del self.__dict_array[index]
                break
        print(self.__dict_array)
        return super().__delitem__(__k)
