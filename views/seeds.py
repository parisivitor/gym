from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from models.execution_type_model import ExecutionTypeModel
from models.exercise_type_model import ExerciseTypeModel
from models.measure_type_model import MeasureTypeModel

router = APIRouter()

@router.get('/seed')
async def seed(db: AsyncSession = Depends(get_session)):
    exercise_types = [
        ExerciseTypeModel(name="ombro"),
        ExerciseTypeModel(name="trapezio"),
        ExerciseTypeModel(name="costas"),
        ExerciseTypeModel(name="peito"),
        ExerciseTypeModel(name="biceps"),
        ExerciseTypeModel(name="triceps"),
        ExerciseTypeModel(name="antebraço"),
        ExerciseTypeModel(name="abdomen"),
        ExerciseTypeModel(name="gluteo"),
        ExerciseTypeModel(name="quadriceps"),
        ExerciseTypeModel(name="posterior"),
        ExerciseTypeModel(name="paturrilha")
    ]

    measure_types = [
        MeasureTypeModel(name="s", description="segundos"),
        MeasureTypeModel(name="min", description="minutos"),
        MeasureTypeModel(name="h", description="horas"),
        MeasureTypeModel(name="kg", description="kilo"),
        MeasureTypeModel(name="m", description="metros"),
        MeasureTypeModel(name="km", description="quilometro"),
        MeasureTypeModel(name="barras", description="quantidade de barras no aparelho")
    ]

    execution_type = [
        ExecutionTypeModel(name="cadencia", description="seguir serie tempo de descanso e cadencia"),
        ExecutionTypeModel(name="progressive overload", description="aumentar gradualmente o peso ou a resistência de um exercício ao longo do tempo para desafiar os músculos e promover o crescimento."),
        ExecutionTypeModel(name="biset", description="realizar dois exercícios consecutivos sem descansar entre eles para aumentar a intensidade do seu treino."),
        ExecutionTypeModel(name="dropset", description="reduzindo gradualmente o peso ou a resistência de um exercício à medida que você cansa, permitindo que você ultrapasse seus limites habituais e aumente a resistência muscular."),
        ExecutionTypeModel(name="circuito", description="realizar uma série de exercícios em uma ordem específica com pouco ou nenhum descanso entre eles para melhorar o condicionamento cardiovascular e a resistência."),
        ExecutionTypeModel(name="pirâmides", description="aumentar gradualmente o peso ou a resistência de um exercício para um determinado número de repetições e, em seguida, diminuir o peso para as séries subsequentes."),
        ExecutionTypeModel(name="isómetrico", description="manter uma posição estática ou contração por um período de tempo para aumentar a força e a resistência muscular."),
        ExecutionTypeModel(name="rest-pause", description="faça descanso de 5 a 15 segundos entre as repetiçoes caso não consiga fazer o numero de series determinado, até atigir o numero de repetiçoes determinado"),
    ]
    try:
        async with db as session:
            session.add_all(exercise_types)
            session.add_all(measure_types)
            session.add_all(execution_type)
            await session.commit()

        return {'message': 'Seed Realizada com sucesso'}
    except:
        HTTPException(status_code=409, detail='Ocorreu algum erro!')