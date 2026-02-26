from dataclasses import dataclass
from typing import List, Optional

# Input Types

@dataclass
class Task:
    id: str
    repair_time: int  # Hours needed for repair work
    inspection_time: int  # Hours needed for quality check


@dataclass
class Resources:
    mechanics: int  # Number of available mechanics
    inspectors: int  # Number of available inspectors
    inspector_capacity: int  # Cars each inspector can check simultaneously

# Output Types

@dataclass
class ScheduleItem:
    task_id: str  # Which car
    mechanic: int  # Which mechanic (0 to mechanics-1)
    repair_start: int  # When repair begins (hour)
    inspection_start: int  # When inspection begins (hour)


@dataclass
class Schedule:
    schedule: List[ScheduleItem]  # When each car is processed
    total_time: int  # Total hours to complete all cars


# Function to implement

def schedule_tasks(tasks: List[Task], resources: Resources) -> Optional[Schedule]:
    """
    Create a schedule for repairing all cars.

    Rules:
    - Each car must complete repair_time hours with a mechanic before starting inspection
    - Each mechanic can only work on one car at a time
    - Each inspector has an inspector_capacity (max cars they can inspect simultaneously)
    - Total cars being inspected at any time ≤ (inspectors × inspector_capacity)

    Args:
        tasks: List of cars to be repaired
        resources: Available resources (mechanics, inspectors, inspector_capacity)

    Returns:
        A valid schedule for completing all repairs or None if no valid schedule exists
    """
    # Your Implementation Here
    max_inspect = resources.inspectors * resources.inspector_capacity
    mechanic_ready_at = [0] * resources.mechanics
    inspect_ready_at = [0] * max_inspect
    max_time = 0
    scheduled_items = []

    for task in tasks:
        m_id = 0
        for i in range(1, len(mechanic_ready_at)):
            if mechanic_ready_at[i] < mechanic_ready_at[m_id]:
                m_id = i

        m_start = mechanic_ready_at[m_id]
        m_end = m_start + task.repair_time

        mechanic_ready_at[m_id] = m_end

        i_id = 0
        for i in range(1, len(inspect_ready_at)):
            if inspect_ready_at[i] < inspect_ready_at[i_id]:
                i_id = i
        i_start = max(m_end, inspect_ready_at[i_id])
        i_end = i_start + task.inspection_time

        inspect_ready_at[i_id] = i_end

        max_time = max(max_time, i_end)

        scheduled_items.append(ScheduleItem(task.id, m_id, m_start, i_start))
    return Schedule(scheduled_items, max_time)



# Test Cases
def test_case_1():
    """Test Case 1"""
    tasks = [
        Task(id="Car_A", repair_time=3, inspection_time=1),
        Task(id="Car_B", repair_time=2, inspection_time=2),
    ]
    resources = Resources(
        mechanics=1,
        inspectors=1,
        inspector_capacity=1,
    )

    result = schedule_tasks(tasks, resources)
    # Expected: Cars repaired sequentially, total_time = 7
    # Car_A: repair[0-3], inspect[3-4]
    # Car_B: repair[3-5], inspect[5-7] (inspector must wait for car to be repaired)

    assert result is not None, "No valid schedule found"
    assert result.total_time <= 7, f"Expected total_time <= 7, got {result.total_time}"

    print(":white_check_mark: Test Case 1 - Passed")
    print(result)


test_case_1()