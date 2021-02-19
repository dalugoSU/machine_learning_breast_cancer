class BreastCancerPrediction:

    def tumor_data(self):
        import numpy as np
        """
        Takes input data to predict if tumor is malignant or benign
        """
        mean_radius = float(input("Enter mean radius: "))
        mean_radius = "{:.3e}".format(mean_radius)

        mean_texture = float(input("Enter mean texture: "))
        mean_texture = "{:.3e}".format(mean_texture)

        mean_perimeter = float(input("Enter mean perimeter: "))
        mean_perimeter = "{:.3e}".format(mean_perimeter)

        mean_area = float(input("Enter mean area: "))
        mean_area = "{:.3e}".format(mean_area)

        mean_smoothness = float(input("Enter mean smoothness: "))
        mean_smoothness = "{:.3e}".format(mean_smoothness)

        mean_compactness = float(input("Enter mean compactness: "))
        mean_compactness = "{:.3e}".format(mean_compactness)

        mean_concavity = float(input("Enter mean concavity: "))
        mean_concavity = "{:.3e}".format(mean_concavity)

        mean_symmetry = float(input("Enter mean symmetry: "))
        mean_symmetry = "{:.3e}".format(mean_symmetry)

        mean_concave_points = float(input("Enter mean concave points: "))
        mean_concave_points = "{:.3e}".format(mean_concave_points)

        mean_fractal_dimension = float(input("Enter mean fractal dimension: "))
        mean_fractal_dimension = "{:.3e}".format(mean_fractal_dimension)

        radius_error = float(input("Enter radius error: "))
        radius_error = "{:.3e}".format(radius_error)

        texture_error = float(input("Enter texture error: "))
        texture_error = "{:.3e}".format(texture_error)

        perimeter_error = float(input("Enter perimeter error: "))
        perimeter_error = "{:.3e}".format(perimeter_error)

        area_error = float(input("Enter area error: "))
        area_error = "{:.3e}".format(area_error)

        smoothness_error = float(input("Enter smoothness error: "))
        smoothness_error = "{:.3e}".format(smoothness_error)

        compactness_error = float(input("Enter compactness error: "))
        compactness_error = "{:.3e}".format(compactness_error)

        concavity_error = float(input("Enter concavity error: "))
        concavity_error = "{:.3e}".format(concavity_error)

        concave_points_error = float(input("Enter concave points error: "))
        concave_points_error = "{:.3e}".format(concave_points_error)

        symmetry_error = float(input("Enter symmetry error: "))
        symmetry_error = "{:.3e}".format(symmetry_error)

        fractal_dimension_error = float(input("Enter fractal dimension error: "))
        fractal_dimension_error = "{:.3e}".format(fractal_dimension_error)

        worst_radius = float(input("Enter worst radius: "))
        worst_radius = "{:.3e}".format(worst_radius)

        worst_texture = float(input("Enter worst texture: "))
        worst_texture = "{:.3e}".format(worst_texture)

        worst_perimeter = float(input("Enter worst perimeter: "))
        worst_perimeter = "{:.3e}".format(worst_perimeter)

        worst_area = float(input("Enter worst area: "))
        worst_area = "{:.3e}".format(worst_area)

        worst_smoothness = float(input("Enter worst smoothness: "))
        worst_smoothness = "{:.3e}".format(worst_smoothness)

        worst_compactness = float(input("Enter worst compactness: "))
        worst_compactness = "{:.3e}".format(worst_compactness)

        worst_concavity = float(input("Enter worst concavity: "))
        worst_concavity = "{:.3e}".format(worst_concavity)

        worst_concave_points = float(input("Enter worst concave points: "))
        worst_concave_points = "{:.3e}".format(worst_concave_points)

        worst_symmetry = float(input("Enter worst symmetry: "))
        worst_symmetry = "{:.3e}".format(worst_symmetry)

        worst_fractal_dimension = float(input("Enter worst fractal dimension: "))
        worst_fractal_dimension = "{:.3e}".format(worst_fractal_dimension)

        return np.array([mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness,
             mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error,
             area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error,
             fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
             worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension])

    def prediction(self, model, cancer_data):

        data = cancer_data.reshape(-1, 30)

        y_prediction = model.predict(data)
        prediction = ""

        if y_prediction[0] == 1:
            prediction = "malignant"
        else:
            prediction = "benign"

        return prediction


new_prediction = BreastCancerPrediction()