% Facts about planets
planet(mercury, rocky, 0.39, 0.38, 0.06, 88).
planet(venus, rocky, 0.72, 0.95, 0.82, 225).
planet(earth, rocky, 1, 1, 1, 365).
planet(mars, rocky, 1.52, 0.53, 0.11, 687).
planet(jupiter, gas_giant, 5.20, 318, 0.41, 4333).
planet(saturn, gas_giant, 9.58, 95, 0.45, 10759).
planet(uranus, ice_giant, 19.22, 14, 0.72, 30687).
planet(neptune, ice_giant, 30.05, 17, 0.67, 60190).

% Rules for categorizing planets
terrestrial(Planet) :- planet(Planet, rocky, _, _, _, _).
gas_giant(Planet) :- planet(Planet, gas_giant, _, _, _, _).
ice_giant(Planet) :- planet(Planet, ice_giant, _, _, _, _).

% Rules for finding planets with specific properties
habitable(Planet) :- planet(Planet, rocky, _, _, _, _), Planet \= earth.
moons(Planet, NumMoons) :- planet(Planet, _, _, _, _, NumMoons).
