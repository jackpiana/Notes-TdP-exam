from dataclasses import dataclass
from datetime import date, datetime


@dataclass(frozen=True, order=True)
class Driver:
    driverId: int
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: date
    nationality: str
    url: str

    def __str__(self):
        return f"{self.forename} {self.surname}"

@dataclass(frozen=True, order=True)
class Result:
    resultId: int
    raceId: int
    driverId: int
    constructorId: int
    number: int
    grid: int
    position: int
    positionText: str
    positionOrder: int
    points: float
    laps: int
    time: str
    milliseconds: int
    fastestLap: int
    rank: int
    fastestLapTime: str
    fastestLapSpeed: str
    statusId: int

    def __str__(self):
        return f"result {self.resultId}"

@dataclass(frozen=True, order=True)
class Circuit:
    circuitId: int
    circuitRef: str
    name: str
    location: str
    country: str
    lat: float
    lng: float
    alt: int
    url: str

    def __str__(self):
        return f"{self.name} {self.country}"

@dataclass(frozen=True, order=True)
class Constructor:
    constructorId: int
    constructorRef: int
    name: int
    nationality: int
    url: int

    def __str__(self):
        return f"{self.name}"

@dataclass(frozen=True, order=True)
class Race:
    raceId: int
    year: int
    round: int
    circuitId: int
    name: str
    date: date
    time: datetime.time
    url: str

    def __str__(self):
        return f"{self.name} {self.year}"


@dataclass(frozen=True, order=True)
class ConstructorStanding:
    constructorStandingsId: int
    raceId: int
    constructorId: int
    points: float
    position: int
    positionText: str
    wins: int

    def __str__(self):
        return f"constructorStandingsId: {self.constructorStandingsId}"

@dataclass(frozen=True, order=True)
class ConstructorResult:
    constructorResultsId: int
    raceId: int
    constructorId: int
    points: float
    status: str

    def __str__(self):
        return f"constructorResultsId: {self.constructorResultsId}"

@dataclass(frozen=True, order=True)
class Qualifying:
    qualifyId: int
    raceId: int
    driverId: int
    constructorId: int
    number: int
    position: int
    q1: str
    q2: str
    q3: str

    def __str__(self):
        return f"qualifyingId: {self.qualifyId}"

@dataclass(frozen=True, order=True)
class Pitstop:
    raceId: int
    driverId: int
    stop: int
    lap: int
    time: datetime.time
    duration: str
    milliseconds: int

    def __str__(self):
        return f"pitstopId: {self.raceId}, {self.driverId}, {self.stop}"

@dataclass(frozen=True, order=True)
class Laptime:
    raceId: int
    driverId: int
    lap: int
    position: int
    time: str
    milliseconds: int

    def __str__(self):
        return f"laptimeId: {self.raceId}, {self.driverId}, {self.lap}"

@dataclass(frozen=True, order=True)
class DriversStanding:
    driverStandingsId: int
    raceId: int
    driverId: int
    points: float
    position: int
    positionText: str
    wins: int

    def __str__(self):
        return f"driversStandingsId: {self.driverStandingsId}"

