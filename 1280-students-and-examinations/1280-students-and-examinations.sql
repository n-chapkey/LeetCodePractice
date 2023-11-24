# Write your MySQL query statement below
SELECT s.student_id, s.student_name, sb.subject_name, IFNULL(grouped.attended_exams,0) AS attended_exams
FROM Students s
CROSS JOIN Subjects sb
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) grouped
ON s.student_id = grouped.student_id AND sb.subject_name = grouped.subject_name
ORDER BY s.student_id, sb.subject_name;

