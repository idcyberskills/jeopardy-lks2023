# LKS Shop

by faishol

---

## Flag

```
LKS{W4F_uS1ng_C5P_and_CSRFTOKEN_st11LL_br0k3n_O00fff}
```

## Description
We sell the most wanted items, "Flag" for today only! Go get it before we ran out of stock.

P.S. Admin has the most money.

## Difficulty
easy

## Hints
> Intentionally left empty

## Tags
xss, csp

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

## Notes
- If running on local, change the `HOST_URL` on the `docker-compose.yml`.
- Change flag inside `src/web/flag.txt`.