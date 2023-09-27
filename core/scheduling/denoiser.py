# pylint: disable=not-callable

from typing import Callable, Union

import torch
from k_diffusion.external import CompVisVDenoiser, CompVisDenoiser

Denoiser = Union[CompVisDenoiser, CompVisVDenoiser]


class _ModelWrapper:
    def __init__(self, alphas_cumprod) -> None:
        self.callable: Callable = None  # type: ignore
        self.alphas_cumprod = alphas_cumprod

    def apply_model(self, *args, **kwargs) -> torch.Tensor:
        if len(args) == 3:
            encoder_hidden_states = args[-1]
            args = args[:2]
        if kwargs.get("cond", None) is not None:
            encoder_hidden_states = kwargs.pop("cond")
        return self.callable(*args, encoder_hidden_states=encoder_hidden_states, return_dict=True, **kwargs)[0]  # type: ignore


def create_denoiser(
    alphas_cumprod: torch.Tensor,
    prediction_type: str,
    device: torch.device = torch.device("cuda"),
    dtype: torch.dtype = torch.float16,
    denoiser_enable_quantization: bool = False,
) -> Denoiser:
    model = _ModelWrapper(alphas_cumprod)
    model.alphas_cumprod = alphas_cumprod
    if prediction_type == "v_prediction":
        denoiser = CompVisVDenoiser(model, quantize=denoiser_enable_quantization)
    else:
        denoiser = CompVisDenoiser(model, quantize=denoiser_enable_quantization)
    denoiser.sigmas = denoiser.sigmas.to(device, dtype)
    denoiser.log_sigmas = denoiser.log_sigmas.to(device, dtype)
    return denoiser
