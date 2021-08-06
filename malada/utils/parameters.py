class Parameters:
    """Holds parameters needed for constructing a data acqusition pipeline."""
    def __init__(self):
        self.temperature = 0
        self.run_system = "bash"
        self.number_of_atoms = 0
        self.crystal_structure = "bcc"
        self.element = None
        self.base_folder = "./"
        self.dft_calculator = "qe"
        self.md_calculator = "qe"
        # TODO: Get number of electrons directly from file.
        self.pseudopotential = {"path": None, "valence_electrons": 0,
                                "name": None}
        self.dft_conv_accuracy_meVperatom = 1
        self.maximum_cutoff_try = 2
        self.maximum_kpoint_try = 2
        self.dft_scf_accuracy_per_atom_Ry = 1e-6
        self.md_at_gamma_point = True
        self.maximum_number_of_timesteps = 10000
        self.time_step_fs = 1
        self.md_thermostat_controller = 0.001
        # TODO: Implement negative values, meaning automatic detection.
        self.snapshot_parsing_beginning = -1
        self.snapshot_parsing_temperature_tolerance_percent = 1
        # TODO: Implement other criteria here.
        self.snapshot_parsing_criterion = "random"
        self.number_of_snapshots = 10
        self.distance_metric_snapshots = "realspace"
        # TODO: Implement negative values, meaning automatic detection.
        self.distance_metric_snapshots_cutoff = -0.1
