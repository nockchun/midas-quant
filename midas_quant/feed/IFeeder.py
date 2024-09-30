from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
import pandas as pd
from .IFeedPart import IFeedPart

class IFeeder(ABC):
    """
    Abstract base class that defines the interface for feeder classes. 
    Feeder classes are responsible for iterating over a collection of data sources 
    (e.g., Pandas DataFrames) and providing windowed segments of data for processing.

    This interface ensures that all feeder implementations adhere to a consistent 
    set of methods, facilitating interoperability and reliability across different feeder types.
    """

    @abstractmethod
    def datas(self) -> List[pd.DataFrame]:
        """
        Retrieves the list of all Pandas DataFrames managed by the feeder.

        Returns:
            List[pd.DataFrame]: The list of DataFrames.
        """
        pass

    @abstractmethod
    def __iter__(self) -> 'IFeeder':
        """
        Resets the feeder to its initial state and returns the iterator object itself.

        Returns:
            IFeeder: The iterator object itself.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Retrieves the total number of windowed segments across all DataFrames.

        Returns:
            int: The total number of windowed segments.
        """
        pass

    @abstractmethod
    def __next__(self) -> Tuple[IFeedPart, bool]:
        """
        Retrieves the next windowed segment and indicates if a DataFrame change has occurred.

        Returns:
            Tuple[IFeedPart, bool]: 
                - IFeedPart: An instance of the feed part containing the windowed DataFrame segment.
                - bool: True if the feeder has moved to a new DataFrame, False otherwise.

        Raises:
            StopIteration: If all DataFrames have been processed.
        """
        pass

    @abstractmethod
    def reset(self) -> None:
        """
        Resets the feeder to its initial state, allowing iteration to start from the beginning.

        Returns:
            None
        """
        pass

    @abstractmethod
    def next(self) -> Tuple[Optional[IFeedPart], Optional[bool]]:
        """
        Retrieves the next windowed segment in a safe manner, returning (None, None) 
        if the iteration has completed.

        Returns:
            Tuple[Optional[IFeedPart], Optional[bool]]: 
                - Optional[IFeedPart]: An instance of the feed part containing the windowed DataFrame segment, or None if iteration is complete.
                - Optional[bool]: True if a DataFrame change has occurred, False if not, or None if iteration is complete.
        """
        pass
