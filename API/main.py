from fastapi import FastAPI
from starlette import responses
from typing import Optional
import pandas as pd



app = FastAPI()



@app.get('/')
def home():
    from lib import leer_html
    
    html = leer_html('home.html')
    return responses.HTMLResponse(content=html, status_code=200)



@app.get('/get_max_duratio/{year}/{platform}/{duration_type}')
def get_max_duration(
                    year: Optional[int]=None, 
                    platform: Optional[str]=None, 
                    duration_type: Optional[str]='min'
                    ):
    if(
        year<1920 
        or year>2021 
        or platform not in ['amazon','disney','hulu','netflix'] 
        or duration_type not in ['min', 'season']
        ):
        
        return ValueError('Parametros Equivocados')
    
    df_plataformas=pd.read_csv('../datasets/plataformas_unique.csv')

    mask = (df_plataformas['duration_type']== duration_type) & (df_plataformas['platform']==platform) & (df_plataformas['release_year'] == year)

    df_aux=df_plataformas[mask]
    max=df_aux['duration_int'].max()
    mask2=df_aux['duration_int']==max
    df_aux=df_aux[mask2]
    
    name=df_aux['title']
    duration=df_aux['duration_int']
    unidad=df_aux['duration_type']
    
    retornar=(name.get(14908), duration.get(14908), unidad.get(14908))
    return retornar



@app.get('/get_score_count/{platform}/{scored}/{release_year}')
def get_score_count(
                    platform, 
                    scored: Optional[float]=None, 
                    release_year: Optional[int]=None
                    ):
    

    if (
        release_year < 1920 
        or release_year > 2021 
        or platform not in ['amazon', 'disney', 'hulu', 'netflix'] 
        or scored > 99 
        or scored < 0
    ):
        raise ValueError('Parametros equivocados')
    
    df_score = pd.read_csv('../datasets/plataformas_withscore.csv')

    mask = (df_score['release_year'] == release_year) & (df_score['score'] > scored) & (df_score['platform'] == platform) & (df_score.type == 'movie')

    df_aux = df_score[mask] 

    cant = df_aux.groupby('platform').size()

    return cant.to_dict()



@app.get('/get_count_platform/{platform}')
def get_count_platform(platform):
    
    if platform not in ['amazon', 'disney', 'hulu', 'netflix']:
        
        return ValueError('Parametro equivocado')

    df_plataformas=pd.read_csv('../datasets/plataformas_unique.csv')

    mask = (df_plataformas['type']== 'movie') & (df_plataformas['platform']==platform)

    df_aux=df_plataformas[mask]
    df_aux=df_aux['id']
    
    cant=len(df_aux)

    return cant



@app.get('/get_actor/{platform}/{year}')
def get_actor(
            platform,
            year
                ):
    year=int(year)
    if (
        year<1920
        or year>2021
        or platform not in ['amazon', 'disney', 'hulu', 'netflix']
    ):
        return ValueError('Parametros equivocados')
    
    df_plataformas=pd.read_csv('../datasets/plataformas_unique.csv')

    platform ='amazon'
    year = 2020
    df_plataformas=pd.read_csv('../datasets/plataformas_unique.csv')

    mask = (df_plataformas['platform']==platform) & (df_plataformas['release_year']==year) & (df_plataformas['cast'] != 'Unknown')
    df_aux = df_plataformas[mask]
    df_aux = df_aux['cast']
    cast= df_aux.str.split(',').explode()
    cant=cast.value_counts()

    maximo = max(cant.items(), key=lambda x: x[1])
    return maximo


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)