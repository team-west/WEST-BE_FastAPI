from fastapi import APIRouter

router = APIRouter(
  prefix='/user'
)

@router.get('/', tags=['get_mypage_info'])
async def get_mypage(user_id: ):
  