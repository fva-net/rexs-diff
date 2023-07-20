components_dict = {
"components" : [ {
      "id" : 1,
      "type" : "gear_unit",
      "name" : "Gear unit [1]",
      "attributes" : [ {
        "id" : "operating_time_vdi_2736_2014",
        "unit" : "h",
        "floating_point" : 100000.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "direction_vector_gravity_u",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "direction_vector_gravity_v",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "direction_vector_gravity_w",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_nodes_in_mesh_width_for_loaddistribution",
        "unit" : "none",
        "integer" : 18
      }, {
        "id" : "account_for_gravity",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "account_for_shear_deformation",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "number_of_gears",
        "unit" : "none",
        "integer" : 7
      }, {
        "id" : "gravitational_acceleration",
        "unit" : "m / s^2",
        "floating_point" : 9.81
      }, {
        "id" : "gear_shift_index",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "operating_time",
        "unit" : "h",
        "floating_point" : 100000.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 0.0 ]
      } ]
    }, {
      "id" : 2,
      "type" : "gear_casing",
      "name" : "Casing [2]",
      "attributes" : [ {
        "id" : "type_of_gear_casing_construction_vdi_2736_2014",
        "unit" : "none",
        "enum" : "closed"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      } ]
    }, {
      "id" : 3,
      "type" : "shaft",
      "name" : "Shaft [3]",
      "attributes" : [ {
        "id" : "rotational_speed",
        "unit" : "1 / min",
        "floating_point" : 2000.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "defines_speed",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 0.0 ]
      } ]
    }, {
      "id" : 13,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [13]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.19500000290572642
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.2
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 88.0
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 14,
      "type" : "shaft",
      "name" : "Shaft [14]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 161.4, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 16,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [16]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 171.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 17
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 22.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : 20.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.95
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 41.69801505542208
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 171.0, 0.0, 0.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.08426421305160345, 0.9964434466635796 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 17,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [17]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 67
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : -20.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.95
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 142.15482597397795
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 171.4, 0.0, 88.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, -0.2941384573017699, 0.9557628199172297 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 19,
      "type" : "shaft",
      "name" : "Shaft [19]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 20.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 21,
      "type" : "switchable_coupling",
      "name" : "Coupling [21]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 141.4
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ True, False, False, False, False, False, True ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 161.4, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 27,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "K 45x52x18 [27]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 7.425
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E15
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E15
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "K 45x52x18"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 151.4
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 171.4, 0.0, 88.0 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E12
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 57.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 30.900000000000002
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 28,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [28]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.19000000283122062
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.2
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 88.0
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 29,
      "type" : "shaft",
      "name" : "Shaft [29]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 111.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 31,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [31]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 120.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 24
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : 22.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.9
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 54.50118426609779
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 120.0, 0.0, 0.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0667532121652842, 0.9977695168051671 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 32,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [32]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 9.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 62
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : -22.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.9
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 129.09981582316823
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 120.0, 0.0, 88.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, -0.32393354795607276, 0.9460798362234505 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 35,
      "type" : "switchable_coupling",
      "name" : "Coupling [35]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 91.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ False, True, False, False, False, False, False ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 111.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 36,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "HK 4518 RS [36]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 5.4
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "HK 4518 RS"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 100.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 120.0, 0.0, 88.0 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E10
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 43.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 20.900000000000002
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 9.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 37,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [37]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : 83.0
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.19000000283122062
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.2
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 94.0
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 16.5
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 38,
      "type" : "shaft",
      "name" : "Shaft [38]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 21.0, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 40,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [40]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 29.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 37
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : 29.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.9
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 85.69779097149438
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 29.0, 0.0, 0.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.1651353585791354, -0.9862709127551823 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 41,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [41]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 8.25
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 50
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 16.5
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : -29.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.9
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 109.91761639385133
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 29.25, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.6243409655287395, -0.7811519434544352 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 43,
      "type" : "shaft",
      "name" : "Shaft [43]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 45,
      "type" : "switchable_coupling",
      "name" : "Coupling [45]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 21.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ False, False, True, False, False, False, False ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 21.0, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 48,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [48]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : 83.0
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.18000000268220903
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.2
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 94.0
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 49,
      "type" : "shaft",
      "name" : "Shaft [49]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 86.0, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 51,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [51]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 95.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 52
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : 28.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.8
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 108.52855674449407
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 95.0, 0.0, 0.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.2032474695590397, -0.9791274003508672 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 52,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [52]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 9.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 41
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : -28.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.8
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 86.7118088749588
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 95.0, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.6848572987574368, -0.7286772127208774 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 54,
      "type" : "switchable_coupling",
      "name" : "Coupling [54]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 95.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 17.474999999999998
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 9.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ False, False, False, True, False, False, False ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 95.0, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 56,
      "type" : "shaft",
      "name" : "Shaft [56]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 86.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 61,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "HK3516-2RS [61]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 2.625
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "HK3516-2RS"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 35.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 75.5
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 95.5, 0.0, 88.0 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E10
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 21.45
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 12.8
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 9.5
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 62,
      "type" : "switchable_coupling",
      "name" : "Coupling [62]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 75.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 16.125
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 9.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ False, False, False, False, True, False, False ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 95.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 63,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [63]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.1600000023841858
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.2
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 88.0
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 64,
      "type" : "shaft",
      "name" : "Shaft [64]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 41.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 66,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [66]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 50.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 54
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : 29.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.6
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 102.73337546425486
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 50.0, 0.0, 0.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.06316176322659163, 0.9980033024324659 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 67,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [67]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 9.1
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 41
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 18.2
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : -29.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.6
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 79.74492584315236
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 50.1, 0.0, 88.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, -0.5141644550439576, 0.8576916189221802 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 69,
      "type" : "switchable_coupling",
      "name" : "Coupling [69]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 21.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ False, False, False, False, False, True, False ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 41.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 70,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [70]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : 129.36600606026718
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.19500000290572642
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 120.68054351346467
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 71,
      "type" : "shaft",
      "name" : "Shaft [71]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 161.4, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 73,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [73]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 50
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : 20.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.95
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 107.03492478496098
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 171.4, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.8255590245206958, -0.5643157777631574 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 77,
      "type" : "switchable_coupling",
      "name" : "Coupling [77]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 161.4
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ False, False, False, False, False, False, True ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 161.4, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 78,
      "type" : "shaft",
      "name" : "Shaft [78]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 185.0, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 80,
      "type" : "switchable_coupling",
      "name" : "Coupling [80]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 17.474999999999998
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 185.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ False, False, True, True, False, False, True ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 185.0, 93.299338254284, 11.455718280084 ]
      } ]
    }, {
      "id" : 82,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [82]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : 15.66603776165084
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.2500000037252903
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.2
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 137.68768554838036
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 27.0
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 83,
      "type" : "shaft",
      "name" : "Shaft [83]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 100.0, 130.479110960584, 144.028578448286 ]
      } ]
    }, {
      "id" : 85,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [85]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 15.0
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 21
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 29.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : 25.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 2.5
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 65.77470659065948
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 200.0, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.6552708617142295, 0.7553940016893774 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 86,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [86]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 99.5
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 78
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 27.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : -25.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 2.5
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 219.6586941976859
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 199.5, 130.479110960584, 144.028578448286 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.25292675088983824, 0.9674854307349078 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 94,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [94]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : -113.239
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.2500000037252903
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.2
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 142.0
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 27.0
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 95,
      "type" : "shaft",
      "name" : "Shaft [95]",
      "attributes" : [ {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 185.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 97,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [97]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 14.75
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 25
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 29.5
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : 25.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 2.5
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 74.34146264589462
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 199.75, 0.0, 88.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.9822453336695864, -0.1876009181329426 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 99,
      "type" : "switchable_coupling",
      "name" : "Coupling [99]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 165.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "is_engaged",
        "unit" : "none",
        "boolean_array" : [ True, True, False, False, True, True, False ]
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 185.0, 0.0, 88.0 ]
      } ]
    }, {
      "id" : 100,
      "type" : "external_load",
      "name" : "Load [100]",
      "attributes" : [ {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "transmits_torque",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "force_u_direction",
        "unit" : "N",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 101,
      "type" : "external_load",
      "name" : "Load [101]",
      "attributes" : [ {
        "id" : "torque_around_u_axis",
        "unit" : "N m",
        "floating_point" : 150.0
      }, {
        "id" : "defines_torque",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 250.0
      }, {
        "id" : "transmits_torque",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "force_u_direction",
        "unit" : "N",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 102,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "K 35x42x16 [102]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 4.75
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "K 35x42x16"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 35.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 29.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 29.0, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E10
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 37.5
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 23.85
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 8.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 103,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "K35X42X16 [103]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 4.75
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "K35X42X16"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 35.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 50.0, 0.0, 88.0 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E10
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 37.5
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 23.85
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 9.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 104,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "K55X60X27 [104]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 12.8
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "K55X60X27"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 179.5
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 199.5, 0.0, 88.0 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E10
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 96.75
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 60.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 36.9
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 27.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 105,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "RNAO 45x55x17 [105]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 5.6000000000000005
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "RNAO 45x55x17"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 95.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 95.0, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E10
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 46.5
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 21.6
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 9.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 17.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 106,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "HK 4518 RS [106]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 5.4
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "HK 4518 RS"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 170.4
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 170.4, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E10
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 43.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 20.900000000000002
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 9.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 107,
      "type" : "rolling_bearing_with_detailed_geometry",
      "name" : "K 47x52x27 [107]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 11.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "radial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "axial_stiffness",
        "unit" : "N / m",
        "floating_point" : 1.0E13
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "K 47x52x27"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "FVA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 47.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 199.5
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 199.5, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "bending_stiffness",
        "unit" : "N mm / rad",
        "floating_point" : 1.0E10
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 83.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_needle_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 34.300000000000004
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 27.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 108,
      "type" : "rolling_bearing_with_catalog_geometry",
      "name" : "N206-E-TVP2 [108]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 5.4
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "N206-E-XL-TVP2"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "INA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 10.0, 0.0, 0.0 ]
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 37.5
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "operating_radial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 62.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 46.0
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_0",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 109,
      "type" : "rolling_bearing_with_catalog_geometry",
      "name" : "6306 [109]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 1.12
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "6306"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "INA"
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "both_directions"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.56
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 193.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 193.0, 0.0, 0.0 ]
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 16.2
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 12.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 72.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_grooved_ball_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 30.5
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 193.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 19.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_0",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 110,
      "type" : "rolling_bearing_with_catalog_geometry",
      "name" : "30306-XL [110]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 8.4
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "30306-XL"
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "INA"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 30.0, 0.0, 88.0 ]
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 61.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 72.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.32
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_tapered_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 77.0
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 20.75
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_0",
        "unit" : "none",
        "floating_point" : 1.05
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 1.9
      } ]
    }, {
      "id" : 111,
      "type" : "rolling_bearing_with_catalog_geometry",
      "name" : "33007 [111]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 8.5
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "33007"
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "INA"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 35.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "positive"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 205.5
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 225.5, 0.0, 88.0 ]
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 70.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 62.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.31
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_tapered_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 53.0
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 225.5
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 21.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_0",
        "unit" : "none",
        "floating_point" : 1.08
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 1.97
      } ]
    }, {
      "id" : 112,
      "type" : "rolling_bearing_with_catalog_geometry",
      "name" : "30206-XL [112]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 7.2
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "30206-XL"
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "INA"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 10.0, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 48.5
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 62.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.37
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_tapered_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 52.0
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 17.25
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_0",
        "unit" : "none",
        "floating_point" : 0.88
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 1.6
      } ]
    }, {
      "id" : 113,
      "type" : "rolling_bearing_with_catalog_geometry",
      "name" : "32007-X-XL [113]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 8.9
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "32007-X-XL"
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "INA"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 35.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "positive"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 224.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 224.0, 93.299338254284, 11.455718280084 ]
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 57.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 62.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.45
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_tapered_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 54.0
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 224.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_0",
        "unit" : "none",
        "floating_point" : 0.73
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 1.32
      } ]
    }, {
      "id" : 114,
      "type" : "rolling_bearing_with_catalog_geometry",
      "name" : "32009-X-XL [114]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 13.3
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "32009-X-XL"
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "INA"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 14.0
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 114.0, 130.479110960584, 144.028578448286 ]
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 86.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 75.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.39
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_tapered_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 72.0
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 114.0
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_0",
        "unit" : "none",
        "floating_point" : 0.84
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 1.53
      } ]
    }, {
      "id" : 115,
      "type" : "rolling_bearing_with_catalog_geometry",
      "name" : "30209-XL [115]",
      "attributes" : [ {
        "id" : "fatigue_limit_load",
        "unit" : "kN",
        "floating_point" : 12.6
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "speed_outer_ring",
        "unit" : "1 / min",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_bearing_rows",
        "unit" : "none",
        "integer" : 1
      }, {
        "id" : "catalogue_designation",
        "unit" : "none",
        "string" : "30209-XL"
      }, {
        "id" : "manufacturer",
        "unit" : "none",
        "string" : "INA"
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "inner_diameter",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "radial_force_absorption",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "axial_force_absorption",
        "unit" : "none",
        "enum" : "positive"
      }, {
        "id" : "radial_factor_x_1",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "misalignment_in_w_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "radial_factor_x_2",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "u_coordinate_on_shaft_inner_side",
        "unit" : "mm",
        "floating_point" : 145.5
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 245.5, 130.479110960584, 144.028578448286 ]
      }, {
        "id" : "radial_static_load_rating",
        "unit" : "kN",
        "floating_point" : 83.0
      }, {
        "id" : "operating_axial_bearing_clearance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "distance_between_bearing_rows",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "preload_distance",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter",
        "unit" : "mm",
        "floating_point" : 85.0
      }, {
        "id" : "catalogue_value_e",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "misalignment_in_v_direction",
        "unit" : "mum",
        "floating_point" : 0.0
      }, {
        "id" : "bearing_type",
        "unit" : "none",
        "enum" : "radial_tapered_roller_bearing"
      }, {
        "id" : "radial_dynamic_load_rating",
        "unit" : "kN",
        "floating_point" : 84.0
      }, {
        "id" : "u_coordinate_on_shaft_outer_side",
        "unit" : "mm",
        "floating_point" : 245.5
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.0, 1.0 ]
      }, {
        "id" : "width",
        "unit" : "mm",
        "floating_point" : 20.75
      }, {
        "id" : "contamination_factor_according_to_iso_281_2007",
        "unit" : "none",
        "floating_point" : 0.5
      }, {
        "id" : "axial_factor_y_1",
        "unit" : "none",
        "floating_point" : 0.0
      }, {
        "id" : "axial_factor_y_0",
        "unit" : "none",
        "floating_point" : 0.81
      }, {
        "id" : "axial_factor_y_2",
        "unit" : "none",
        "floating_point" : 1.48
      } ]
    }, {
      "id" : 116,
      "type" : "cylindrical_stage",
      "name" : "Cylindrical stage [116]",
      "attributes" : [ {
        "id" : "lubrication_type_vdi_2736_2014",
        "unit" : "none",
        "enum" : "circulating_oil"
      }, {
        "id" : "mesh_load_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "coefficient_of_friction_is_determined_according_to_vdi_2736_2014",
        "unit" : "none",
        "boolean" : True
      }, {
        "id" : "design_safety_factor_flank_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "design_safety_factor_root_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 3.0
      }, {
        "id" : "maximum_permissible_material_exposure_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.8
      }, {
        "id" : "overload_factor_agma_2101_c95",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "temperature_lubricant",
        "unit" : "C",
        "floating_point" : 60.0
      }, {
        "id" : "face_load_factor_flank_din_3990_1987",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_spiral_angle_factor_vdi_2736_2014",
        "unit" : "none",
        "enum" : "din_3990_1987"
      }, {
        "id" : "flag_designation_addendum_modification",
        "unit" : "none",
        "enum" : "entry_of_addendum_modification_coefficient"
      }, {
        "id" : "determination_of_factor_for_tooth_flank_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "rotating_angle_around_neg_u_axis",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "wear_coefficient_vdi_2736_2014",
        "unit" : "1e-6 mm^3 / (N m)",
        "floating_point" : 1.0
      }, {
        "id" : "determination_of_factor_for_tooth_root_loading_vdi_2736_2014",
        "unit" : "none",
        "enum" : "equals_application_factor"
      }, {
        "id" : "permissible_linear_wear_vdi_2736_2014",
        "unit" : "mm",
        "floating_point" : 0.18000000268220903
      }, {
        "id" : "determination_of_wear_coefficient_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "face_load_factor_flank_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.2
      }, {
        "id" : "center_distance_tolerance_field_din_3964_1980",
        "unit" : "none",
        "enum" : "7"
      }, {
        "id" : "center_distance",
        "unit" : "mm",
        "floating_point" : 88.0
      }, {
        "id" : "determination_of_scuffing_temperature_agma_925_a03",
        "unit" : "none",
        "enum" : "is_given"
      }, {
        "id" : "determination_of_degree_of_tooth_loss_vdi_2736_2014",
        "unit" : "none",
        "enum" : "according_to_wimmer"
      }, {
        "id" : "application_factor_for_fatigue_load_vdi_2736_2014",
        "unit" : "none",
        "floating_point" : 1.4
      }, {
        "id" : "common_face_width",
        "unit" : "mm",
        "floating_point" : 16.0
      }, {
        "id" : "application_factor_iso_6336_2006",
        "unit" : "none",
        "floating_point" : 1.4
      } ]
    }, {
      "id" : 117,
      "type" : "cylindrical_gear",
      "name" : "Cylindrical gear [117]",
      "attributes" : [ {
        "id" : "averaged_peak_to_valley_height_flank",
        "unit" : "mum",
        "floating_point" : 5.0
      }, {
        "id" : "reference_component_for_position",
        "unit" : "none",
        "reference_component" : 1
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 9.5
      }, {
        "id" : "determination_of_hardness_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_c1"
      }, {
        "id" : "number_of_teeth",
        "unit" : "none",
        "integer" : 35
      }, {
        "id" : "determination_of_poissons_ratio_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "averaged_peak_to_valley_height_root",
        "unit" : "mum",
        "floating_point" : 20.0
      }, {
        "id" : "is_adequate_profile_modfication_iso_6336_2019",
        "unit" : "none",
        "boolean" : False
      }, {
        "id" : "width_to_normal_module_ratio",
        "unit" : "none",
        "floating_point" : 20.0
      }, {
        "id" : "determination_of_residual_stress_depth_profile_iso_6336_2019",
        "unit" : "none",
        "enum" : "method_b"
      }, {
        "id" : "determination_of_yield_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "width_to_diameter_ratio",
        "unit" : "none",
        "floating_point" : 2.0
      }, {
        "id" : "face_width",
        "unit" : "mm",
        "floating_point" : 19.0
      }, {
        "id" : "determination_of_modulus_of_elasticity_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "helix_angle_reference_diameter",
        "unit" : "°",
        "floating_point" : -28.0
      }, {
        "id" : "normal_module",
        "unit" : "mm",
        "floating_point" : 1.8
      }, {
        "id" : "tip_diameter",
        "unit" : "mm",
        "floating_point" : 74.70287400851394
      }, {
        "id" : "datum_face_orientation",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "support_vector",
        "unit" : "mm",
        "floating_point_array" : [ 95.5, 0.0, 88.0 ]
      }, {
        "id" : "number_of_points_in_y_direction_iso_6336_2019",
        "unit" : "none",
        "integer" : 10
      }, {
        "id" : "determination_of_fatigue_strength_under_pulsating_stress_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "tooth_thickness_deviation_tolerance_series_din_3967_1978",
        "unit" : "none",
        "enum" : "c25"
      }, {
        "id" : "arithmetic_average_roughness_flank",
        "unit" : "mum",
        "floating_point" : 0.8333333333333334
      }, {
        "id" : "chamfer_at_tooth_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "y_coordinate_of_maximum_hardness_iso_6336_2019",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "arithmetic_average_roughness_root",
        "unit" : "mum",
        "floating_point" : 3.3333333333333335
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "material_exposure_calibration_factor_iso_6336_2019",
        "unit" : "none",
        "floating_point" : 0.04
      }, {
        "id" : "u_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 1.0, 0.0, 0.0 ]
      }, {
        "id" : "w_axis_vector",
        "unit" : "mm",
        "floating_point_array" : [ 0.0, 0.9379214001996965, 0.34684787306172243 ]
      }, {
        "id" : "determination_of_rolling_contact_fatigue_strength_vdi_2736_2014",
        "unit" : "none",
        "enum" : "is_taken_from_material"
      }, {
        "id" : "depth_of_case_hardening_at_550_hv",
        "unit" : "mm",
        "floating_point" : 0.3
      }, {
        "id" : "required_minimum_safety_factor_root_plewe_1980",
        "unit" : "none",
        "floating_point" : 1.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      } ]
    }, {
      "id" : 120,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [120]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 121,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [121]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 122,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [122]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 123,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [123]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 124,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [124]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 125,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [125]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 126,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [126]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 127,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [127]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 128,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [128]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 129,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [129]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 130,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [130]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 131,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [131]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 132,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [132]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 133,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [133]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 134,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [134]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 135,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [135]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 136,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [136]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 137,
      "type" : "cylindrical_stage_gear_data",
      "name" : "Cylindrical stage gear data [137]",
      "attributes" : [ {
        "id" : "is_driving_gear",
        "unit" : "none",
        "boolean" : False
      } ]
    }, {
      "id" : 496,
      "type" : "rack_shaped_tool",
      "name" : "Tool [496]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 497,
      "type" : "rack_shaped_tool",
      "name" : "Tool [497]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 498,
      "type" : "rack_shaped_tool",
      "name" : "Tool [498]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 499,
      "type" : "rack_shaped_tool",
      "name" : "Tool [499]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 500,
      "type" : "rack_shaped_tool",
      "name" : "Tool [500]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 501,
      "type" : "rack_shaped_tool",
      "name" : "Tool [501]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 502,
      "type" : "rack_shaped_tool",
      "name" : "Tool [502]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 503,
      "type" : "rack_shaped_tool",
      "name" : "Tool [503]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 504,
      "type" : "rack_shaped_tool",
      "name" : "Tool [504]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 505,
      "type" : "rack_shaped_tool",
      "name" : "Tool [505]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 506,
      "type" : "rack_shaped_tool",
      "name" : "Tool [506]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 507,
      "type" : "rack_shaped_tool",
      "name" : "Tool [507]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 508,
      "type" : "rack_shaped_tool",
      "name" : "Tool [508]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 509,
      "type" : "rack_shaped_tool",
      "name" : "Tool [509]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 510,
      "type" : "rack_shaped_tool",
      "name" : "Tool [510]",
      "attributes" : [ {
        "id" : "tip_radius_factor",
        "unit" : "none",
        "floating_point" : 0.25
      }, {
        "id" : "utilized_dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "dedendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.3
      }, {
        "id" : "chamfer_angle",
        "unit" : "°",
        "floating_point" : 30.0
      }, {
        "id" : "addendum_coefficient_reference_profile",
        "unit" : "none",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1208,
      "type" : "material",
      "name" : "G20Mn5 [1208]",
      "attributes" : [ {
        "id" : "core_hardness_vickers",
        "unit" : "HV",
        "floating_point" : 550.0
      }, {
        "id" : "density",
        "unit" : "kg / dm^3",
        "floating_point" : 7.85
      }, {
        "id" : "surface_hardness_brinell",
        "unit" : "HB",
        "floating_point" : 266.0
      }, {
        "id" : "elastic_modulus",
        "unit" : "N / mm^2",
        "floating_point" : 210000.0
      }, {
        "id" : "material_designation",
        "unit" : "none",
        "string" : "G20Mn5"
      }, {
        "id" : "thermal_expansion_coefficient_plus",
        "unit" : "1e-6 / C",
        "floating_point" : 11.0
      }, {
        "id" : "fatigue_limit_torsion",
        "unit" : "MPa",
        "floating_point" : 120.0
      }, {
        "id" : "heat_treated_material_type_iso_6336_2006",
        "unit" : "none",
        "enum" : "normalized_cast_steel"
      }, {
        "id" : "material_category_vdi_2736_2014",
        "unit" : "none",
        "enum" : "steel"
      }, {
        "id" : "yield_strength",
        "unit" : "N / mm^2",
        "floating_point" : 300.0
      }, {
        "id" : "surface_hardness_vickers",
        "unit" : "HV",
        "floating_point" : 750.0
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 262.92
      }, {
        "id" : "fatigue_limit_bending",
        "unit" : "MPa",
        "floating_point" : 200.0
      }, {
        "id" : "thermal_capacity",
        "unit" : "J / (kg K)",
        "floating_point" : 430.0
      }, {
        "id" : "fatigue_limit_compression_tension",
        "unit" : "MPa",
        "floating_point" : 170.0
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 655.28
      }, {
        "id" : "poisson_ratio",
        "unit" : "none",
        "floating_point" : 0.3
      }, {
        "id" : "tensile_strength",
        "unit" : "N / mm^2",
        "floating_point" : 500.0
      }, {
        "id" : "thermal_conductivity",
        "unit" : "W / (m K)",
        "floating_point" : 40.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 525.84
      }, {
        "id" : "thermal_expansion_coefficient_minus",
        "unit" : "1e-6 / C",
        "floating_point" : -8.0
      } ]
    }, {
      "id" : 1209,
      "type" : "material",
      "name" : "42CrMo4 [1209]",
      "attributes" : [ {
        "id" : "core_hardness_vickers",
        "unit" : "HV",
        "floating_point" : 550.0
      }, {
        "id" : "density",
        "unit" : "kg / dm^3",
        "floating_point" : 7.85
      }, {
        "id" : "surface_hardness_brinell",
        "unit" : "HB",
        "floating_point" : 266.0
      }, {
        "id" : "elastic_modulus",
        "unit" : "N / mm^2",
        "floating_point" : 210000.0
      }, {
        "id" : "material_designation",
        "unit" : "none",
        "string" : "42CrMo4"
      }, {
        "id" : "thermal_expansion_coefficient_plus",
        "unit" : "1e-6 / C",
        "floating_point" : 11.0
      }, {
        "id" : "fatigue_limit_torsion",
        "unit" : "MPa",
        "floating_point" : 315.0
      }, {
        "id" : "heat_treated_material_type_iso_6336_2006",
        "unit" : "none",
        "enum" : "through_hardened_wrought_steel"
      }, {
        "id" : "material_category_vdi_2736_2014",
        "unit" : "none",
        "enum" : "steel"
      }, {
        "id" : "yield_strength",
        "unit" : "N / mm^2",
        "floating_point" : 900.0
      }, {
        "id" : "surface_hardness_vickers",
        "unit" : "HV",
        "floating_point" : 750.0
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 306.0
      }, {
        "id" : "fatigue_limit_bending",
        "unit" : "MPa",
        "floating_point" : 525.0
      }, {
        "id" : "thermal_capacity",
        "unit" : "J / (kg K)",
        "floating_point" : 430.0
      }, {
        "id" : "fatigue_limit_compression_tension",
        "unit" : "MPa",
        "floating_point" : 495.0
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 740.64
      }, {
        "id" : "poisson_ratio",
        "unit" : "none",
        "floating_point" : 0.3
      }, {
        "id" : "tensile_strength",
        "unit" : "N / mm^2",
        "floating_point" : 1100.0
      }, {
        "id" : "thermal_conductivity",
        "unit" : "W / (m K)",
        "floating_point" : 40.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 612.0
      }, {
        "id" : "thermal_expansion_coefficient_minus",
        "unit" : "1e-6 / C",
        "floating_point" : -8.0
      } ]
    }, {
      "id" : 1210,
      "type" : "material",
      "name" : "16MnCr5 [1210]",
      "attributes" : [ {
        "id" : "core_hardness_vickers",
        "unit" : "HV",
        "floating_point" : 550.0
      }, {
        "id" : "density",
        "unit" : "kg / dm^3",
        "floating_point" : 7.85
      }, {
        "id" : "surface_hardness_brinell",
        "unit" : "HB",
        "floating_point" : 693.5
      }, {
        "id" : "elastic_modulus",
        "unit" : "N / mm^2",
        "floating_point" : 210000.0
      }, {
        "id" : "material_designation",
        "unit" : "none",
        "string" : "16MnCr5"
      }, {
        "id" : "thermal_expansion_coefficient_plus",
        "unit" : "1e-6 / C",
        "floating_point" : 11.0
      }, {
        "id" : "fatigue_limit_torsion",
        "unit" : "MPa",
        "floating_point" : 255.0
      }, {
        "id" : "heat_treated_material_type_iso_6336_2006",
        "unit" : "none",
        "enum" : "case_hardened_wrought_steel"
      }, {
        "id" : "material_category_vdi_2736_2014",
        "unit" : "none",
        "enum" : "steel"
      }, {
        "id" : "yield_strength",
        "unit" : "N / mm^2",
        "floating_point" : 695.0
      }, {
        "id" : "surface_hardness_vickers",
        "unit" : "HV",
        "floating_point" : 750.0
      }, {
        "id" : "endurance_limit_root",
        "unit" : "N / mm^2",
        "floating_point" : 461.0
      }, {
        "id" : "fatigue_limit_bending",
        "unit" : "MPa",
        "floating_point" : 430.0
      }, {
        "id" : "thermal_capacity",
        "unit" : "J / (kg K)",
        "floating_point" : 430.0
      }, {
        "id" : "fatigue_limit_compression_tension",
        "unit" : "MPa",
        "floating_point" : 400.0
      }, {
        "id" : "endurance_limit_flank",
        "unit" : "N / mm^2",
        "floating_point" : 1500.0
      }, {
        "id" : "poisson_ratio",
        "unit" : "none",
        "floating_point" : 0.3
      }, {
        "id" : "tensile_strength",
        "unit" : "N / mm^2",
        "floating_point" : 1000.0
      }, {
        "id" : "thermal_conductivity",
        "unit" : "W / (m K)",
        "floating_point" : 40.0
      }, {
        "id" : "basic_strength_root",
        "unit" : "N / mm^2",
        "floating_point" : 922.0
      }, {
        "id" : "thermal_expansion_coefficient_minus",
        "unit" : "1e-6 / C",
        "floating_point" : -8.0
      } ]
    }, {
      "id" : 1211,
      "type" : "lubricant",
      "name" : "ISO-VG-220 [1211]",
      "attributes" : [ {
        "id" : "density_at_15_degree_celsius",
        "unit" : "kg / dm^3",
        "floating_point" : 0.9
      }, {
        "id" : "viscosity_at_100_degree_celsius",
        "unit" : "mm^2 / s",
        "floating_point" : 19.0
      }, {
        "id" : "name",
        "unit" : "none",
        "string" : "ISO-VG-220"
      }, {
        "id" : "viscosity_at_40_degree_celsius",
        "unit" : "mm^2 / s",
        "floating_point" : 220.0
      }, {
        "id" : "lubricant_type_iso_6336_2006",
        "unit" : "none",
        "enum" : "mineral_oil"
      } ]
    }, {
      "id" : 1350,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1350]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 41
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 38.5
      } ]
    }, {
      "id" : 1351,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1351]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 41
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 38.5
      } ]
    }, {
      "id" : 1352,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1352]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 86
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 57.5
      } ]
    }, {
      "id" : 1353,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1353]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 37
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 50.0
      } ]
    }, {
      "id" : 1354,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1354]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 52
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 48.5
      } ]
    }, {
      "id" : 1355,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1355]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 74
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 49.5
      } ]
    }, {
      "id" : 1356,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1356]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 11
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 46.0
      } ]
    }, {
      "id" : 1357,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1357]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "both_directions"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 8
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 6.24
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 6.36
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 51.0
      } ]
    }, {
      "id" : 1358,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1358]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 12.04
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 17
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 46.0
      } ]
    }, {
      "id" : 1359,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1359]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "positive"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 11.68
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 18
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 50.01
      } ]
    }, {
      "id" : 1360,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1360]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 13.86
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 17
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 46.0
      } ]
    }, {
      "id" : 1361,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1361]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "positive"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 16.7
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 18
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 50.01
      } ]
    }, {
      "id" : 1362,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1362]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "negative"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 14.57
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 22
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 60.0
      } ]
    }, {
      "id" : 1363,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1363]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "positive"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 14.93
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 22
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 60.0
      } ]
    }, {
      "id" : 1364,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1364]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 52
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 48.5
      } ]
    }, {
      "id" : 1365,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1365]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 52
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 48.5
      } ]
    }, {
      "id" : 1366,
      "type" : "rolling_bearing_row",
      "name" : "Bearing row [1366]",
      "attributes" : [ {
        "id" : "axial_force_absorption_of_row",
        "unit" : "none",
        "enum" : "no_direction"
      }, {
        "id" : "pressure_angle",
        "unit" : "°",
        "floating_point" : 0.0
      }, {
        "id" : "number_of_rolling_elements",
        "unit" : "none",
        "integer" : 41
      }, {
        "id" : "position_of_rolling_elements",
        "unit" : "none",
        "enum" : "one_rolling_element_on_v_axis"
      }, {
        "id" : "raceway_radius_of_inner_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "raceway_radius_of_outer_ring",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "reference_diameter",
        "unit" : "mm",
        "floating_point" : 38.5
      } ]
    }, {
      "id" : 1368,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1369,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1370,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1371,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1372,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1373,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1374,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1375,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1376,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1377,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1378,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1379,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1380,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1381,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1382,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1383,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1384,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1385,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1386,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1387,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1388,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1389,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1390,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1391,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1392,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1393,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1394,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1395,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1396,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1397,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1398,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1399,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1400,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1401,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1402,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1403,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1404,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1405,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1406,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1407,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1408,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1409,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1410,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1411,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1412,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1413,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1414,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1415,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1416,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1417,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1418,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1419,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1420,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1421,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1422,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1423,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1424,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1425,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1426,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1427,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1428,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1429,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1430,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1431,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1432,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1433,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1434,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1435,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1436,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1437,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1438,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1439,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1440,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1441,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1442,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1443,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1444,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1445,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1446,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1447,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1448,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1449,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1450,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1451,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1452,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1453,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1454,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1455,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1456,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1457,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1458,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1459,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1460,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1461,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1462,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1463,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1464,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1465,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1466,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1467,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1468,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1469,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1470,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1471,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1472,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1473,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1474,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1475,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1476,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1477,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1478,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1479,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1480,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1481,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1482,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1483,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1484,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1485,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1486,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1487,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1488,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1489,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1490,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1491,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1492,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1493,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1494,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1495,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1496,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1497,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1498,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1499,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1500,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1501,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1502,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1503,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1504,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1505,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1506,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1507,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1508,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1509,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1510,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1511,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1512,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1513,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1514,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1515,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1516,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1517,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1518,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1519,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1520,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1521,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1522,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1523,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1524,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1525,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1526,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1527,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1528,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1529,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1530,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1531,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1532,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1533,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1534,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1535,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1536,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1537,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1538,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1539,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1540,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1541,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1542,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1543,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1544,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1545,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1546,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1547,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1548,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1549,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1550,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1551,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1552,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1553,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1554,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1555,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1556,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1557,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1558,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1559,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1560,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1561,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1562,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1563,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1564,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1565,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1566,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1567,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1568,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1569,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1570,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1571,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1572,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1573,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1574,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1575,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1576,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1577,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1578,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1579,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1580,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1581,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1582,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1583,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1584,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1585,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1586,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1587,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1588,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1589,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1590,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1591,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1592,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1593,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1594,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1595,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1596,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1597,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1598,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1599,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1600,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1601,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1602,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1603,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1604,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1605,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1606,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1607,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1608,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1609,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1610,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1611,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1612,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1613,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1614,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1615,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1616,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1617,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1618,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1619,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1620,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1621,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1622,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1623,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1624,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1625,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1626,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1627,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1628,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1629,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1630,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1631,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1632,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1633,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1634,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1635,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1636,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1637,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1638,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1639,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1640,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1641,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1642,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1643,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1644,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1645,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1646,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1647,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1648,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1649,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1650,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1651,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1652,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1653,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1654,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1655,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1656,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1657,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1658,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1659,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1660,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1661,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1662,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1663,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1664,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1665,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1666,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1667,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1668,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1669,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1670,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1671,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1672,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1673,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1674,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1675,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1676,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1677,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1678,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1679,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1680,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1681,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1682,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1683,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1684,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1685,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1686,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1687,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1688,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1689,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1690,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1691,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1692,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1693,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1694,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1695,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1696,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1697,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1698,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1699,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1700,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1701,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1702,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1703,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1704,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1705,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1706,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1707,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1708,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1709,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1710,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1711,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1712,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1713,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1714,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1715,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1716,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1717,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 13.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 2.5
      } ]
    }, {
      "id" : 1718,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1719,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1720,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1721,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1722,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1723,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1724,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1725,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1726,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1727,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1728,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1729,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1730,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1731,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1732,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1733,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1734,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1735,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1736,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1737,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1738,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1739,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1740,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1741,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1742,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1743,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1744,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1745,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1746,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1747,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1748,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1749,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1750,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1751,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1752,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1753,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1754,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1755,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1756,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1757,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1758,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1759,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1760,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1761,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1762,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1763,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1764,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1765,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1766,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1767,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1768,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1769,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.4
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.75
      } ]
    }, {
      "id" : 1770,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1771,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1772,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1773,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1774,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1775,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1776,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1777,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1778,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1779,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1780,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1781,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1782,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1783,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1784,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1785,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1786,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1787,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1788,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1789,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1790,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1791,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1792,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1793,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1794,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1795,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1796,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1797,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1798,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1799,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1800,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1801,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1802,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1803,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1804,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1805,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1806,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1807,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1808,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1809,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1810,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1811,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1812,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1813,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1814,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1815,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1816,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1817,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1818,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1819,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1820,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1821,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1822,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1823,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1824,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1825,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1826,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1827,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1828,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1829,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1830,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1831,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1832,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1833,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1834,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1835,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1836,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1837,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1838,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1839,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1840,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1841,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1842,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1843,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 21.6
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 1.25
      } ]
    }, {
      "id" : 1844,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1845,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1846,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1847,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1848,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1849,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1850,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1851,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1852,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1853,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1854,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 9.5
      } ]
    }, {
      "id" : 1855,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.0
      } ]
    }, {
      "id" : 1856,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.0
      } ]
    }, {
      "id" : 1857,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.0
      } ]
    }, {
      "id" : 1858,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.0
      } ]
    }, {
      "id" : 1859,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.0
      } ]
    }, {
      "id" : 1860,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.0
      } ]
    }, {
      "id" : 1861,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.0
      } ]
    }, {
      "id" : 1862,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 12.0
      } ]
    }, {
      "id" : 1863,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1864,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1865,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1866,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1867,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1868,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1869,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1870,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1871,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1872,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1873,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1874,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1875,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1876,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1877,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1878,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1879,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1880,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1881,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1882,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1883,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1884,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1885,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1886,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1887,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1888,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1889,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1890,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1891,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1892,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1893,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1894,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1895,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1896,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1897,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1898,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1899,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1900,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1901,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1902,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1903,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1904,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1905,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1906,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1907,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1908,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1909,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1910,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1911,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1912,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1913,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1914,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 10.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.5
      } ]
    }, {
      "id" : 1915,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1916,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1917,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1918,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1919,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1920,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1921,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1922,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1923,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1924,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1925,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1926,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1927,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1928,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1929,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1930,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1931,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1932,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 11.8
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1933,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1934,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1935,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1936,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1937,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1938,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1939,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1940,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1941,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1942,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1943,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1944,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1945,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1946,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1947,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1948,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1949,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1950,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1951,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1952,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1953,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1954,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1955,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1956,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1957,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1958,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1959,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1960,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1961,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1962,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1963,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1964,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1965,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1966,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1967,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1968,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1969,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1970,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1971,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1972,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1973,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1974,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1975,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1976,
      "type" : "rolling_element",
      "attributes" : [ {
        "id" : "mean_operating_temperature",
        "unit" : "C",
        "floating_point" : 20.0
      }, {
        "id" : "length_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 14.5
      }, {
        "id" : "diameter_of_rolling_element",
        "unit" : "mm",
        "floating_point" : 7.0
      } ]
    }, {
      "id" : 1977,
      "type" : "shaft_section",
      "name" : "section [1977]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 30.0
      } ]
    }, {
      "id" : 1978,
      "type" : "shaft_section",
      "name" : "section [1978]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 36.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 90.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 36.0
      } ]
    }, {
      "id" : 1979,
      "type" : "shaft_section",
      "name" : "section [1979]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 44.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 110.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 44.0
      } ]
    }, {
      "id" : 1980,
      "type" : "shaft_section",
      "name" : "section [1980]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 130.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 30.0
      } ]
    }, {
      "id" : 1981,
      "type" : "shaft_section",
      "name" : "section [1981]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 31.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 160.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 22.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 31.0
      } ]
    }, {
      "id" : 1982,
      "type" : "shaft_section",
      "name" : "section [1982]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 182.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 26.5
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 30.0
      } ]
    }, {
      "id" : 1983,
      "type" : "shaft_section",
      "name" : "section [1983]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 24.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 208.5
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 8.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 29.0
      } ]
    }, {
      "id" : 1984,
      "type" : "shaft_section",
      "name" : "section [1984]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 24.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 216.5
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 24.0
      } ]
    }, {
      "id" : 1985,
      "type" : "shaft_section",
      "name" : "section [1985]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 60.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 60.0
      } ]
    }, {
      "id" : 1986,
      "type" : "shaft_section",
      "name" : "section [1986]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 21.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 30.0
      } ]
    }, {
      "id" : 1987,
      "type" : "shaft_section",
      "name" : "section [1987]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 36.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 21.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 70.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 36.0
      } ]
    }, {
      "id" : 1988,
      "type" : "shaft_section",
      "name" : "section [1988]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 91.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 73.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 45.0
      } ]
    }, {
      "id" : 1989,
      "type" : "shaft_section",
      "name" : "section [1989]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 50.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 164.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 1.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 50.0
      } ]
    }, {
      "id" : 1990,
      "type" : "shaft_section",
      "name" : "section [1990]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 165.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 55.0
      } ]
    }, {
      "id" : 1991,
      "type" : "shaft_section",
      "name" : "section [1991]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 35.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 195.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 35.0
      } ]
    }, {
      "id" : 1992,
      "type" : "shaft_section",
      "name" : "section [1992]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 60.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 60.0
      } ]
    }, {
      "id" : 1993,
      "type" : "shaft_section",
      "name" : "section [1993]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 50.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 16.5
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 50.0
      } ]
    }, {
      "id" : 1994,
      "type" : "shaft_section",
      "name" : "section [1994]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 21.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 30.0
      } ]
    }, {
      "id" : 1995,
      "type" : "shaft_section",
      "name" : "section [1995]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 35.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 21.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 65.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 35.0
      } ]
    }, {
      "id" : 1996,
      "type" : "shaft_section",
      "name" : "section [1996]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 86.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 99.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 45.0
      } ]
    }, {
      "id" : 1997,
      "type" : "shaft_section",
      "name" : "section [1997]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 47.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 185.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 47.0
      } ]
    }, {
      "id" : 1998,
      "type" : "shaft_section",
      "name" : "section [1998]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 35.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 215.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 35.0
      } ]
    }, {
      "id" : 1999,
      "type" : "shaft_section",
      "name" : "section [1999]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 70.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 18.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 70.0
      } ]
    }, {
      "id" : 2000,
      "type" : "shaft_section",
      "name" : "section [2000]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 19.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 55.0
      } ]
    }, {
      "id" : 2001,
      "type" : "shaft_section",
      "name" : "section [2001]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 42.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 18.2
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 55.0
      } ]
    }, {
      "id" : 2002,
      "type" : "shaft_section",
      "name" : "section [2002]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 70.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 20.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 70.0
      } ]
    }, {
      "id" : 2003,
      "type" : "shaft_section",
      "name" : "section [2003]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 53.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 52.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 30.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 53.0
      } ]
    }, {
      "id" : 2004,
      "type" : "shaft_section",
      "name" : "section [2004]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 24.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 45.0
      } ]
    }, {
      "id" : 2005,
      "type" : "shaft_section",
      "name" : "section [2005]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 85.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 24.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 10.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 55.0
      } ]
    }, {
      "id" : 2006,
      "type" : "shaft_section",
      "name" : "section [2006]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 111.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 34.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 24.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 85.0
      } ]
    }, {
      "id" : 2007,
      "type" : "shaft_section",
      "name" : "section [2007]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 111.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 58.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 55.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 111.0
      } ]
    }, {
      "id" : 2008,
      "type" : "shaft_section",
      "name" : "section [2008]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 150.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 113.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 7.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 150.0
      } ]
    }, {
      "id" : 2009,
      "type" : "shaft_section",
      "name" : "section [2009]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 111.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 120.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 7.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 111.0
      } ]
    }, {
      "id" : 2010,
      "type" : "shaft_section",
      "name" : "section [2010]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 85.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 127.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 8.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 111.0
      } ]
    }, {
      "id" : 2011,
      "type" : "shaft_section",
      "name" : "section [2011]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 45.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 135.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 24.0
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 45.0
      } ]
    }, {
      "id" : 2012,
      "type" : "shaft_section",
      "name" : "section [2012]",
      "attributes" : [ {
        "id" : "inner_diameter_end",
        "unit" : "mm",
        "floating_point" : 60.0
      }, {
        "id" : "outer_diameter_end",
        "unit" : "mm",
        "floating_point" : 61.0
      }, {
        "id" : "inner_diameter_begin",
        "unit" : "mm",
        "floating_point" : 60.0
      }, {
        "id" : "u_coordinate_on_shaft",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "length",
        "unit" : "mm",
        "floating_point" : 29.5
      }, {
        "id" : "outer_diameter_begin",
        "unit" : "mm",
        "floating_point" : 61.0
      } ]
    }, {
      "id" : 2013,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2014,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2015,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : -0.2
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2016,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : -0.2
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2017,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2018,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2019,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2020,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2021,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2022,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : 0.4
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2023,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2024,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2025,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : -0.3
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2026,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : -0.3
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2027,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2028,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2029,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : 0.23362
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2030,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : 0.23362
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2031,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2032,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2033,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2034,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2035,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2036,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2037,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : -0.1
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2038,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "addendum_modification_coefficient",
        "unit" : "none",
        "floating_point" : -0.1
      }, {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2039,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2040,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2041,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2042,
      "type" : "cylindrical_gear_flank",
      "attributes" : [ {
        "id" : "tooth_tip_chamfer",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "normal_pressure_angle",
        "unit" : "°",
        "floating_point" : 20.0
      } ]
    }, {
      "id" : 2043,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2044,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2045,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2046,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2047,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2048,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2049,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2050,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2051,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2052,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2053,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2054,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2055,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2056,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    }, {
      "id" : 2057,
      "type" : "cylindrical_gear_manufacturing_settings",
      "attributes" : [ {
        "id" : "machining_allowance",
        "unit" : "mm",
        "floating_point" : 0.0
      }, {
        "id" : "generated_addendum_modification_coefficient",
        "unit" : "none"
      }, {
        "id" : "machining_allowance_tolerance",
        "unit" : "mm",
        "floating_point" : 0.0
      } ]
    } ]
  }




for component in components_dict["components"]:
    attributes = component["attributes"]
    for attribute in attributes:
        if len(attribute) != 3:
            print(f"Attribute '{attribute['id']}' in component '{component['id']}' does not have 3 elements.")