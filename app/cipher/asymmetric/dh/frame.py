from ....base.content_tab import TabbedFrame
from .frames.aes_demo import AesGcmDemoTab
from .frames.agreement import AgreementTab
from .frames.key_gen import KeyGenTab
from .frames.params_gen import ParamsGenTab


class Frame(TabbedFrame):
    tab_specs = [
        (ParamsGenTab, "Parameters"),
        (KeyGenTab, "Key Generation"),
        (AgreementTab, "Key Agreement"),
        (AesGcmDemoTab, "AES-GCM Demo"),
    ]
