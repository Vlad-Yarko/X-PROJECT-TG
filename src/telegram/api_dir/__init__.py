from pyrogram.types import Message
from pyrogram.filters import chat, video, photo, media_group
from pyrogram import Client
from src.telegram.api_dir.handlers.zyscel_d.zyscel_h import reg_z
from src.telegram.api_dir.handlers.casual_italy_h.ci_h import reg_c
from src.telegram.api_dir.handlers.keshkatura.keshkatura_h import reg_k

app = Client(
    name="my_app",
    api_hash="6e5d9a7b8f0663e2c9e3d97bb25a3f26",
    api_id="12170540"
)

reg_z(app)
reg_c(app)
reg_k(app)
