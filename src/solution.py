## Student Name:
## Student ID: 

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.

    """
    # TODO: Implement this function
    total: Dict[str, Number] = {}

    for request in requests:
        if not isinstance(request, dict):
            raise ValueError("Malformed Request")
    
        for resource, amount in request.items():
            if amount < 0:
                return False
            
            total[resource] = total.get(resource, 0) + amount

            if resource not in resources:
                return False
            if total[resource] > resources[resource]:
                return False
            
    return True
    # raise NotImplementedError("suggest_slots function has not been implemented yet")