import pybamm

from pybop.models.base_model import BaseModel


class ExponentialDecay(BaseModel):
    """
    exponential decay model with two parameters y0 and k

    dy/dt = -ky
    y(0) = y0

    """

    def __init__(
        self,
        name: str = "Constant Model",
        parameters: pybamm.ParameterValues = None,
    ):
        super().__init__()
        self.pybamm_model = pybamm.BaseModel()
        y = pybamm.Variable("y")
        k = pybamm.Parameter("k")
        y0 = pybamm.Parameter("y0")
        self.pybamm_model.rhs = {y: -k * y}
        self.pybamm_model.initial_conditions = {y: y0}
        self.pybamm_model.variables = {"y": y, "2y": 2 * y}

        default_parameter_values = pybamm.ParameterValues(
            {
                "k": 0.1,
                "y0": 1,
            }
        )

        self._unprocessed_model = self.pybamm_model
        self.name = name

        self.default_parameter_values = (
            default_parameter_values if parameters is None else parameters
        )
        self._parameter_set = self.default_parameter_values
        self._unprocessed_parameter_set = self._parameter_set

        self.geometry = None
        self.submesh_types = None
        self.var_pts = None
        self.spatial_methods = None
        self.solver = pybamm.CasadiSolver(mode="fast")
        self._model_with_set_params = None
        self._built_model = None
        self._built_initial_soc = None
        self._mesh = None
        self._disc = None
