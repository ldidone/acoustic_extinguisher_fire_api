# Acoustic extinguisher fire API

Code repository to acoustic extinguisher fire API with academic purposes.

-------------------------------------------------------------------------

- API documentation is available here: https://acousticextinguisherfireapi.herokuapp.com/docs

**Exaple Curl:**

    curl -X 'POST' \
      'https://acousticextinguisherfireapi.herokuapp.com/predict' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "size": 1,
      "fuel": "gasoline",
      "distance": 10,
      "desibel": 96,
      "airflow": 2.6,
      "frequency": 70
    }'
	

-------------------------------------------------------------------------

> ### Citation
> Yavuz Selim TASPINAR, Murat KOKLU and Mustafa ALTIN CV:https://www.muratkoklu.com/en/publications/ DATASET: https://www.muratkoklu.com/datasets/ Citation Request : 1: KOKLU M., TASPINAR Y.S., (2021). Determining the Extinguishing Status of Fuel Flames With Sound Wave by Machine Learning Methods. IEEE Access, 9, pp.86207-86216, Doi: 10.1109/ACCESS.2021.3088612 Link: https://ieeexplore.ieee.org/document/9452168 (Open Access) https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9452168

> 2: TASPINAR Y.S., KOKLU M., ALTIN M., (2021). Classification of Flame Extinction Based on Acoustic Oscillations using Artificial Intelligence Methods. Case Studies in Thermal Engineering, 28, 101561, Doi: 10.1016/j.csite.2021.101561 Link: https://www.sciencedirect.com/science/article/pii/S2214157X21007243 (Open Access) https://www.sciencedirect.com/sdfe/reader/pii/S2214157X21007243/pdf

> 3: TASPINAR Y.S., KOKLU M., ALTIN M., (2022). Acoustic-Driven Airflow Flame Extinguishing System Design and Analysis of Capabilities of Low Frequency in Different Fuels. Fire Technology, Doi: 10.1007/s10694-021-01208-9 Link: https://link.springer.com/content/pdf/10.1007/s10694-021-01208-9.pdf3: TASPINAR Y.S., KOKLU M., ALTIN M., (2022). Acoustic-Driven Airflow Flame Extinguishing System Design and Analysis of Capabilities of Low Frequency in Different Fuels. Fire Technology, Doi: 10.1007/s10694-021-01208-9 Link: https://link.springer.com/content/pdf/10.1007/s10694-021-01208-9.pdf
