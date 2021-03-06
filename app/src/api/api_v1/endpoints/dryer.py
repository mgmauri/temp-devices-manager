from typing import Any, Optional

from fastapi import APIRouter, Depends
from fastapi.param_functions import Query
from src.api.dependencies import get_gpio_output_drivers_service
from src.api.exceptions import EvkNameNotFound
from src.core.configs import OperationConfig
from src.services.gpio_service import GpioOutputDriversService

router = APIRouter()


@router.post("/drivers/dryers/{evk_name}/air_blast")
def air_blast_by_evk(
    evk_name: str,
    duration: Optional[float] = Query(
        OperationConfig.config.air_blast_default_duration(),
        gt=0,
        lt=OperationConfig.config.air_blast_max_duration(),
    ),
    gpio_output_drivers_service: GpioOutputDriversService = Depends(
        get_gpio_output_drivers_service
    ),
) -> Any:
    if gpio_output_drivers_service.is_valid_evk(evk_name):
        return gpio_output_drivers_service.negative_pulse_by_evk(evk_name, duration)
    else:
        raise EvkNameNotFound


@router.get("/drivers/dryers/{evk_name}/state")
def get_dryer_state_by_evk(
    evk_name: str,
    gpio_output_drivers_service: GpioOutputDriversService = Depends(
        get_gpio_output_drivers_service
    ),
) -> Any:
    if gpio_output_drivers_service.is_valid_evk(evk_name):
        return gpio_output_drivers_service.get_value_by_evk(evk_name)
    else:
        raise EvkNameNotFound


@router.put("/drivers/dryers/{evk_name}/state")
def set_dryer_state_by_evk(
    evk_name: str,
    value: bool,
    gpio_output_drivers_service: GpioOutputDriversService = Depends(
        get_gpio_output_drivers_service
    ),
) -> Any:
    if gpio_output_drivers_service.is_valid_evk(evk_name):
        return gpio_output_drivers_service.set_value_by_evk(evk_name, value)
    else:
        raise EvkNameNotFound


@router.get("/drivers/dryers/states")
def get_dryers_states(
    gpio_output_drivers_service: GpioOutputDriversService = Depends(
        get_gpio_output_drivers_service
    ),
) -> Any:
    return gpio_output_drivers_service.get_all_gpio_outputs_value()
