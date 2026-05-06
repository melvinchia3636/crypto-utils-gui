from ...helpers.content_tab import TabbedFrame
from .frames.params_gen import ParamsGenTab
from .frames.key_gen import KeyGenTab
from .frames.agreement import AgreementTab
from .frames.aes_demo import AesGcmDemoTab


class Frame(TabbedFrame):
    tab_specs = [
        (ParamsGenTab, "Parameters"),
        (KeyGenTab, "Key Generation"),
        (AgreementTab, "Key Agreement"),
        (AesGcmDemoTab, "AES-GCM Demo"),
    ]
