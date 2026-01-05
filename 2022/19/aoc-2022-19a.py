#!/usr/bin/env python3

import re


def bfs(cost_ore, cost_clay, cost_obs_ore, cost_obs_clay, cost_geo_ore, cost_geo_obs):
    nq = set([(0, 0, 0, 0, 0, 0, 1, 0)])
    minutes_left = 24
    max_geode = 0
    max_ore_r = max(cost_ore, cost_clay, cost_obs_ore, cost_geo_ore)
    while minutes_left >= 0:
        q = nq
        nq = set()
        for geode_r, geode, obs_r, obs, clay_r, clay, ore_r, ore in q:
            max_geode = max(geode, max_geode)
            max_needed_ore = minutes_left * max_ore_r
            max_needed_clay = minutes_left * cost_obs_clay
            max_needed_obs = minutes_left * cost_geo_obs

            # continue saving
            nq.add(
                (
                    geode_r,
                    geode + geode_r,
                    obs_r,
                    min(obs + obs_r, max_needed_obs),
                    clay_r,
                    min(clay + clay_r, max_needed_clay),
                    ore_r,
                    min(ore + ore_r, max_needed_ore),
                )
            )

            # buy ore robot
            if ore >= cost_ore and ore_r < max_ore_r and ore < max_needed_ore:
                nq.add(
                    (
                        geode_r,
                        geode + geode_r,
                        obs_r,
                        min(obs + obs_r, max_needed_obs),
                        clay_r,
                        min(clay + clay_r, max_needed_clay),
                        ore_r + 1,
                        min(ore + ore_r - cost_ore, max_needed_ore),
                    )
                )

            # buy clay robot
            if ore >= cost_clay and clay_r < cost_obs_clay and clay < max_needed_clay:
                nq.add(
                    (
                        geode_r,
                        geode + geode_r,
                        obs_r,
                        min(obs + obs_r, max_needed_obs),
                        clay_r + 1,
                        min(clay + clay_r, max_needed_clay),
                        ore_r,
                        min(ore + ore_r - cost_clay, max_needed_ore),
                    )
                )

            # buy obsidian robot
            if (
                ore >= cost_obs_ore
                and clay >= cost_obs_clay
                and obs_r < cost_geo_obs
                and obs < max_needed_obs
            ):
                nq.add(
                    (
                        geode_r,
                        geode + geode_r,
                        obs_r + 1,
                        min(obs + obs_r, max_needed_obs),
                        clay_r,
                        min(clay + clay_r - cost_obs_clay, max_needed_clay),
                        ore_r,
                        min(ore + ore_r - cost_obs_ore, max_needed_ore),
                    )
                )

            # buy geode robot
            if ore >= cost_geo_ore and obs >= cost_geo_obs:
                nq.add(
                    (
                        geode_r + 1,
                        geode + geode_r,
                        obs_r,
                        min(obs + obs_r - cost_geo_obs, max_needed_obs),
                        clay_r + 1,
                        min(clay + clay_r, max_needed_clay),
                        ore_r,
                        min(ore + ore_r - cost_geo_ore, max_needed_ore),
                    )
                )
        minutes_left -= 1
    return max_geode


total = 0
with open(0) as f:
    for line in f:
        (
            bp,
            cost_ore,
            cost_clay,
            cost_obs_ore,
            cost_obs_clay,
            cost_geo_ore,
            cost_geo_obs,
        ) = map(int, re.findall(r"\d+", line.strip()))
        geodes = bfs(
            cost_ore,
            cost_clay,
            cost_obs_ore,
            cost_obs_clay,
            cost_geo_ore,
            cost_geo_obs,
        )
        print(bp, geodes)
        total += bp * geodes
print(total)
