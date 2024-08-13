[GlobalParams]
  displacements = 'disp_x disp_y disp_z'
  volumetric_locking_correction = true
  order = FIRST
  family = LAGRANGE
[]
  
[Mesh]
  [initial]
    type = FileMeshGenerator
    file = mesh/3D_3l.e
  []
[]
  
[Functions]
  [push_down]
    type = PiecewiseLinear
    xy_data = '0  0
         1   -0.226
         1.5  0'
  []
[]
  
[AuxVariables]
  [saved_x]
  []
  [saved_y]
  []
  [saved_z]
  []
  [effective_plastic_strain]
    order = CONSTANT
    family = MONOMIAL
  []
[]
  
[AuxKernels]
  [effective_plastic_strain]
    type = ADMaterialRealAux
    variable = effective_plastic_strain
    property = effective_plastic_strain
    block = 1
  []
[]
  
[Physics/SolidMechanics/QuasiStatic]
  [all]
    add_variables = true
    strain = FINITE
    block = '1 2'
    use_automatic_differentiation = true
    generate_output = 'stress_xx stress_xy stress_xz stress_yy stress_zz vonmises_stress'
    save_in = 'saved_x saved_y saved_z'
    use_finite_deform_jacobian = true
    #decomposition_method = EigenSolution
  []
[]
  
[BCs]
  [specimen_y]
    type = DirichletBC
    variable = disp_y
    boundary = 1
    value = 0.0
  []
  
  [indenter_0]
    type = DirichletBC
    variable = disp_z
    boundary = 2
    value = 0.0
  []
  [specimen_0]
    type = DirichletBC
    variable = disp_z
    boundary = 6
    value = 0.0
  []
  [InclinedNoDisplacementBC]
    [indenter_60]
    boundary = 3
    penalty = 1e5#1e10
    displacements = 'disp_x disp_y disp_z'
    []
    [specimen_60]
    boundary = 7
    penalty = 1e5#1e10
    displacements = 'disp_x disp_y disp_z'
    []
  []
  
  [indenter_y]
    type = FunctionDirichletBC
    variable = disp_y
    boundary = 8
    function = push_down
  []
[]
  
[Materials]
  [tensor]
    type = ADComputeIsotropicElasticityTensor
    block = '2'
    youngs_modulus = 1143
    poissons_ratio = 0.0691
  []
  [stress]
    type = ADComputeFiniteStrainElasticStress
    block = '2'
  []
  
  [tensor_2]
    type = ADComputeIsotropicElasticityTensor
    block = '1'
    youngs_modulus = 114
    poissons_ratio = 0.25
  []
  [power_law_hardening]
    type = ADIsotropicPowerLawHardeningStressUpdate
    strength_coefficient = 1.910 #K
    strain_hardening_exponent = 0.104 #n
    block = '1'
  []
  [radial_return_stress]
    type = ADComputeMultipleInelasticStress
    inelastic_models = 'power_law_hardening'
    block = '1'
  []
[]
  
[Postprocessors]
  [stress_yy]
    type = ElementAverageValue
    variable = stress_yy
    block = 1
  []
  [react_y_top]
    type = NodalSum
    variable = saved_y
    boundary = 8
  []
  [disp_y_top]
    type = NodalExtremeValue
    variable = disp_y
    boundary = 8
  []
[]
  
#[VectorPostprocessors]
#  [y_disp]
#  type = NodalValueSampler
#  variable = disp_y
#  block = 1
#  sort_by = y
#  []
#[]
  
[Executioner]
  type = Transient
  solve_type = 'PJFNK'
  
  petsc_options_iname = '-pc_type -pc_factor_mat_solver_type'
  petsc_options_value = 'lu  superlu_dist'
  line_search = 'none'
  petsc_options = '-snes_ksp_ew'
  
  l_max_its = 20
  nl_max_its = 50
  dt = 0.01 #0.025
  dtmin = 0.00001
  end_time = 1.5
  nl_rel_tol = 1e-6
  nl_abs_tol = 1e-20
  automatic_scaling = true
  [Predictor]
    type = SimplePredictor
    scale = 1.0
    skip_times_old = 1.0
  []
  
[]
  
[Outputs]
  [./my_checkpoint]
    type = Checkpoint
    time_step_interval = 50
  [../]
  exodus = true
  csv = true
  print_linear_residuals = true
  print_perf_log = true
  [./console]
    type = Console
    max_rows = 5
  [../]
[]
  
[Preconditioning]
  [./smp]
    type = SMP
    full = true
  [../]
[]
  
[Dampers]
  [contact_slip]
    type = ContactSlipDamper
    primary = '5'
    secondary = '4'
    min_damping_factor = 0.01
  []
  [jacobian]
    type = ElementJacobianDamper
    max_increment = 0.01
  []
[]
  
[Contact]
  [ind_base]
    primary = 5
    secondary = 4
    model = coulomb
    friction_coefficient = 0.4
    normalize_penalty = true
    formulation = penalty #tangential_penalty
    penalty = 1e5#1e6
    #capture_tolerance = 1e-4
    tangential_tolerance = 1e-1
  []
[]
  
