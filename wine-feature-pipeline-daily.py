import os
import modal

LOCAL=False

if LOCAL == False:
   stub = modal.Stub("wine_daily")
   image = modal.Image.debian_slim().pip_install(["hopsworks"]) 

   @stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("dani-hopsworks-ai"))
   def f():
       g()
def generate_wine(quality, alcohol_max, alcohol_min,
                  sulphates_max, sulphates_min,
                  volatile_acidity_max, volatile_acidity_min,
                  total_sulfur_dioxide_max, total_sulfur_dioxide_min,
                  ph_max, ph_min,
                  density_max, density_min,
                  free_sulfur_dioxide_max, free_sulfur_dioxide_min,
                  chlorides_max, chlorides_min,
                  residual_sugar_max, residual_sugar_min,
                  citric_acid_max, citric_acid_min,
                  fixed_acidity_max, fixed_acidity_min
                  ):
    """
    Returns a single wine as a single row in a DataFrame
    """
    import pandas as pd
    import random
    df = pd.DataFrame({"alcohol": [random.uniform(alcohol_max, alcohol_min)],
                       "sulphates": [random.uniform(sulphates_max, sulphates_min)],
                       "volatile_acidity": [random.uniform(volatile_acidity_max, volatile_acidity_min)],
                       "total_sulfur_dioxide": [random.randint(total_sulfur_dioxide_min, total_sulfur_dioxide_max)],
                       "ph": [random.uniform(ph_max, ph_min)],
                       "density": [random.uniform(density_max, density_min)],
                       "free_sulfur_dioxide": [random.randint(free_sulfur_dioxide_min, free_sulfur_dioxide_max)],
                       "chlorides": [random.uniform(chlorides_max, chlorides_min)],
                       "residual_sugar": [random.uniform(residual_sugar_max, residual_sugar_min)],
                       "citric_acid": [random.uniform(citric_acid_max, citric_acid_min)],
                       "fixed_acidity": [random.uniform(fixed_acidity_max, fixed_acidity_min)]
                      })
    df['qualitybin'] = quality
    return df


def get_random_wine():
    """
    Returns a DataFrame containing one random wine
    """
    import pandas as pd
    import random
    qual = str(random.randint(0, 1))
    newWine_df = generate_wine(qual, 14.9, 8.0,
                               2.0, 0.22,
                               1.58, 0.08,
                               440, 6,
                               14, 0,
                               1.1, 0.5,
                               290, 1,
                               1,0,
                               70,0,
                               2,0,
                               16,3)



    print("new wine added with quality: " + str(qual))


    return newWine_df


def g():
    import hopsworks
    import pandas as pd

    project = hopsworks.login()
    fs = project.get_feature_store()

    wine_df = get_random_wine()

    wine_fg = fs.get_feature_group(name="wine",version=1)
    wine_fg.insert(wine_df)

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        stub.deploy("wine_daily")
        with stub.run():
            f()
