# Home

This documentation providers a high-level overview of Django-Wohn, aka Melive.xyz, project.

# Progress so far

## General

- [x] Start using milestones based on weeks, [here](https://github.com/dmpe/django-wohn/milestone)

## DevOps environment
- [x] Setup working DevOps working environment
- [x] On commit, pushed automatically through CI/CD to Docker Registry (DockerHub, now moved to [Quay.io](https://quay.io/user/dmpe))
  - [x] Project can be build and deployed to VM
- [ ] Write proper API documentation, see [issue 75](https://github.com/dmpe/django-wohn/issues/75)
- [x] Speed up on current environment, like [here 72](https://github.com/dmpe/django-wohn/issues/72)

## Features

- [x] Azure Function for fetching forex data (ECB for USD/EUR and CNB for CZK)
  - [ ] See its branch -> Integrate into workflow

- [x] Split Backend from Frontend for simpler maintainance
    - [x] Provide [GraphQL API](https://github.com/dmpe/django-wohn/issues/54) for majority of functions
    - [ ] Setup Frontend to talk to Backend
       - GraphQL
- [x] Website: Login (username and admin) and Logout with Social Media
  - [x] Does not use GraphQL - uses Django templates, etc.
  - Flow 1: User can register and see his admin site/panel
  - Flow 2: User can login and logout
- [ ] Website: Add new blog or news section
- [x] Website: "About us" Site
    - [x] Rendered from `readme.md` file
- [x] Website: Fix all issues that inhibit smooth feature-complete as of the last time
- [ ]
- [ ] Emails: Avoid DJango, but when needed transition to SendGrid's API.
- [x] Posting a real-estate:
    - [x] DJango Model Inheritance via [Abstract Class](https://docs.djangoproject.com/en/2.2/topics/db/models/#model-inheritance)
        - Rooms, Houses, Apartments
- [ ]
- [ ]
- [ ]
