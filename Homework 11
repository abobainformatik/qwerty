import pandas as pd

def chickenpox_by_sex(data):


  grouped = data.groupby('sex')
  vaccinated_counts = grouped['vaccine'].sum()
  chickenpox_counts = grouped['chickenpox'].sum()

  
  ratios = chickenpox_counts / vaccinated_counts


  return ratios.to_dict()



data = pd.read_csv('chickenpox_data.csv')


ratios = chickenpox_by_sex(data)


print(ratios)
