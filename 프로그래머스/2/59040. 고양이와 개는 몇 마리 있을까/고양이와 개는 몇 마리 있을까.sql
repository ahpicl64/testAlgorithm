-- 코드를 입력하세요
SELECT animal_type, count(*) as count
from animal_ins
group by animal_type
order by 
    case
        when animal_type = 'cat' then 1
        else 2
    end