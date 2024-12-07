from typing import TypedDict

class SupportState(TypedDict):
        name: str
        issue : str
        solution_approved :bool
        solution : str
        inspection_count : int
        
    