% --- Database Facts ---
% Format: person(Name, date(Year, Month, Day)).

person('Alice Smith', date(2008, 5, 12)).
person('Bob Jones', date(2007, 11, 23)).
person('Charlie Brown', date(2009, 2, 14)).
person('Diana Prince', date(2006, 8, 30)).

% --- Helper Rules ---

% Find a person's date of birth by name
get_dob(Name, DOB) :-
    person(Name, DOB).

% Find people born in a specific year
born_in_year(Year, Name) :-
    person(Name, date(Year, _, _)).