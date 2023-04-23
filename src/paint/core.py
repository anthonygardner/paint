"""Core physics for point masses and rigid bodies
"""
from typing import Self

from paint.structs import Vector3


class RigidBody:
    def __init__(
            self,
            forces: List[Vector3],
            moments: List[Vector3],
    ) -> Self:
        self._force_at_cg: Vector3
        self._moment_at_cg: Vector3

    @property
    def force_at_cg(self) -> Vector3:
        return self._force_at_cg

    @property
    def moment_cog(self) -> Vector3:
        return self._moment_at_cg

    def sum_forces_at_cg(
        forces: List[Vector3],
        distances: List[Vector3],
    ) -> Vector3:
        force_at_cg = Vector3.zeros

        for force in forces:
            force_at_cg += force


def moment_transport_theorem(
    Rq: Vector3,
    Rqp: Vector3,
    Fq: Vector3,
    Mqp: Vector3,
    ) -> Vector3:
    """Applies moment transport theorem on Fq to obtain Mq

    """
    dR = Rqp - Rq
    Mq = Mqp + math.cross(dR, Fq)
    return Mq

def parallel_axis_theorem() -> float:
    pass        

