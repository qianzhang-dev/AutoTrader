from functools import partial
from typing import Dict, List, Set
from flask_sqlalchemy import SQLAlchemy

from . import default_controller as dc
from .. import at_db


class ControllerMeta(type):
    """Metaclass for dispatching the default_controller routes onto sub-controllers (e.g. ping_controller)
    """
    RegisterdMethodMappings: Dict[str, classmethod] = {}
    WhiteListedVerbs: Set[str] = { 'option', 'get', 'post', 'put', 'patch', 'delete' }

    def __new__(cls, name, bases, dct):
        super().__new__(cls, name, bases, dct)

        # Exposed class attribute
        cls.db: SQLAlchemy = at_db
        
        # Register
        methods: List[str] = [d for d in dct.keys() if isinstance(dct[d], classmethod)]
        verb_methods: List[str] = [d for d in methods if ControllerMeta._is_verb_method(d)]
        for vm in verb_methods:
            if ControllerMeta._is_method_in_default_controller(vm):
                ControllerMeta._register_verb_method(vm, dct[vm], cls)
        
        return cls
    
    @staticmethod
    def _is_verb_method(name: str) -> bool:
        if name.find('_') == -1:
            return False
        
        verb = name.split('_')[0]
        return verb in ControllerMeta.WhiteListedVerbs

    @staticmethod
    def _is_method_in_default_controller(name: str) -> bool:
        return getattr(dc, name, None) is not None
    
    @staticmethod
    def _register_verb_method(name: str, method: classmethod, cls) -> bool:
        if name not in ControllerMeta.RegisterdMethodMappings.keys():
            ControllerMeta.RegisterdMethodMappings[name] = method
            setattr(dc, name, partial(method.__func__, cls))
        else:
            raise Exception(f'Already registered {name} in controller_meta')