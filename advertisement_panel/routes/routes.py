from pydantic import BaseModel,EmailStr
from fastapi import status,APIRouter,HTTPException, Depends
from datetime import datetime
from config.database import get_database,Database
from models.api_logs import metadata,posts
from datetime import date


router=APIRouter()

class Advertisement(BaseModel):
    id:int
    title:str
    description:str
    photo:str
    start_date:date
    end_date:date
    campaign_start_date:date
    campaign_end_date:date
    created_date:datetime
    updated_date:datetime



@router.post("/advertisement_panel", status_code=status.HTTP_201_CREATED)
async def advertisement(user: Advertisement):
    try:
        db = get_database()
        insert_query = posts.insert().values(id=user.id,
                                             title=user.title,
                                             description=user.description,
                                             photo=user.photo,
                                             start_date=user.start_date,
                                             end_date=user.end_date,
                                             campaign_start_date=user.campaign_start_date,
                                             campaign_end_date=user.campaign_end_date,
                                             created_date=user.created_date,
                                             updated_date=user.updated_date
                                                    )

        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')  

    
@router.get("/advertisement-data")
async def retrieve_info():
    select_stmt = posts.select()
    result = await get_database().fetch_all(select_stmt)
    return result


@router.get("/individual_data")
async def retrieve_advmt_info(id: int):
    db = get_database()
    select_query = posts.select().where(posts.c.id == id)
    result = await db.fetch_one(select_query)
    #print(result)
    return result

@router.patch("/posts/{id}")
async def update_post(
    post:Advertisement,
    database: Database = Depends(get_database),
):
    update_query = (
        posts.update()
        .where(posts.c.id == post.id)
        .values(post.dict(exclude_unset=True))
    )
    await database.execute(update_query)
    # post_db = await get_post_or_404(post.id, database)
    return "updated succesfully"

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post:Advertisement, database: Database = Depends(get_database)
):
    delete_query = posts.delete().where(posts.c.id == post.id)
    await database.execute(delete_query)

