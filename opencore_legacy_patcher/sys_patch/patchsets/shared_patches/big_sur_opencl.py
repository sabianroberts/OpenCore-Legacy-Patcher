"""
big_sur_opencl.py: Big Sur OpenCL patches
"""

from .base import BaseSharedPatchSet

from ..base import PatchType

from ....datasets.os_data import os_data


class BigSurOpenCL(BaseSharedPatchSet):

    def __init__(self, xnu_major: int, xnu_minor: int, marketing_version: str) -> None:
        super().__init__(xnu_major, xnu_minor, marketing_version)


    def _os_requires_patches(self) -> bool:
        """
        Check if the current OS requires
        """
        return self._xnu_major >= os_data.monterey.value


    def patches(self) -> dict:
        """
        For graphics cards dropped in Monterey
        """
        if self._os_requires_patches() is False:
            return {}

        return {
            "Big Sur OpenCL": {
                PatchType.MERGE_SYSTEM_VOLUME: {
                    "/System/Library/Frameworks": {
                        "OpenCL.framework": "11.6",
                    },
                },
            },
        }