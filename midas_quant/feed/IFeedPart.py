from abc import ABC, abstractmethod
from typing import Union
import pandas as pd

class IFeedPart(ABC):
    """
    Abstract base class that defines the interface for feed parts. It includes methods for data access,
    value comparison, and detecting cross events between columns in a dataset.

    Any subclass inheriting from FeedPart must implement all abstract methods to ensure consistent behavior.
    """

    @abstractmethod
    def __getitem__(self, index: Union[int, slice]) -> Union[pd.Series, pd.DataFrame]:
        """
        Allows for both integer and slice indexing on the data.

        Args:
            index (Union[int, slice]): Can be an integer for single-row access or a slice object for range access.

        Returns:
            Union[pd.Series, pd.DataFrame]: The row(s) of the data at the specified index/indices.
        """
        pass

    @abstractmethod
    def upCompare(self, index: int, target: str, compare: str) -> bool:
        """
        Compares whether the target column value is greater than the compare column value at a specific index.

        Args:
            index (int): The index to compare values.
            target (str): The target column to compare.
            compare (str): The column to compare against the target.

        Returns:
            bool: True if the target column's value is greater than the compare column's value, else False.
        """
        pass

    @abstractmethod
    def downCompare(self, index: int, target: str, compare: str) -> bool:
        """
        Compares whether the target column value is less than the compare column value at a specific index.

        Args:
            index (int): The index to compare values.
            target (str): The target column to compare.
            compare (str): The column to compare against the target.

        Returns:
            bool: True if the target column's value is less than the compare column's value, else False.
        """
        pass

    @abstractmethod
    def upValue(self, index: int, target: str, value: float) -> bool:
        """
        Checks if the target column value is greater than a specified value at a specific index.

        Args:
            index (int): The index to check.
            target (str): The target column to check.
            value (float): The value to compare against.

        Returns:
            bool: True if the target column's value is greater than the specified value, else False.
        """
        pass

    @abstractmethod
    def downValue(self, index: int, target: str, value: float) -> bool:
        """
        Checks if the target column value is less than a specified value at a specific index.

        Args:
            index (int): The index to check.
            target (str): The target column to check.
            value (float): The value to compare against.

        Returns:
            bool: True if the target column's value is less than the specified value, else False.
        """
        pass

    @abstractmethod
    def betweenValue(self, index: int, target: str, value: float, percent: float = 1.0) -> bool:
        """
        Checks if the target column value is within a percentage range of a specified value at a specific index.

        Args:
            index (int): The index to check.
            target (str): The target column to check.
            value (float): The value to compare against.
            percent (float, optional): The percentage range around the value (default is 1.0%).

        Returns:
            bool: True if the target column's value is within the range of (value - percent%) 
                  and (value + percent%), else False.
        """
        pass

    @abstractmethod
    def cross(self, index: int, target: str, compare: str, updn: str = "up") -> bool:
        """
        Detects if a 'cross' event occurs between the target and compare columns at a specific index.
        A 'cross' event is when the target column value crosses above (or below) the compare column value.

        Args:
            index (int): The index to check.
            target (str): The target column to compare.
            compare (str): The compare column to check against.
            updn (str, optional): A string indicating the direction of the cross event:
                                   "up" for crossing from below to above,
                                   "down" for crossing from above to below.
                                   Defaults to "up".

        Returns:
            bool: True if the 'cross' event occurs at the specified index, else False.

        Raises:
            ValueError: If the `updn` parameter is neither "up" nor "down".
            AssertionError: If the index is out of bounds based on the direction (backward or forward).
        """
        pass

