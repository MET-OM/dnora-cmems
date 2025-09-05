from dnora.modelrun.modelrun import ModelRun
from dnora.type_manager.dnora_types import DnoraDataType
import dnora_cmems.waterlevel


class Global(ModelRun):
    _reader_dict = {
        DnoraDataType.WATERLEVEL: dnora_cmems.waterlevel.Global(),
    }
