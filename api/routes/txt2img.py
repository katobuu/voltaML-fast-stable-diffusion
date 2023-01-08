from fastapi import APIRouter, HTTPException

from api.shared import state
from core import queue
from core.types import Txt2ImgQueueEntry
from core.utils import convert_image_to_base64

router = APIRouter()


@router.post("/interupt")
async def stop():
    "Interupt the current job"

    state.interrupt = True
    return {"message": "Interupted"}


@router.post("/generate")
async def txt2img_job(job: Txt2ImgQueueEntry):
    "Generate images from text"
    # Create directory to save images if it does not exist

    if job.backend == "PyTorch":
        images, time = await queue.generate(job)
    elif job.backend == "TensorRT":
        images, time = await queue.generate(job)
        # infer_trt()
    else:
        raise HTTPException(status_code=400, detail="Invalid backend")

    return {
        "message": "Job completed",
        "time": time,
        "images": [convert_image_to_base64(i) for i in images],
    }
