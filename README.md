# The tech talent redirect machine

The ATTP project has a domain name (`atlantatechtalentpipeline.com`) which
sole purpose is to redirect to
`https://www.thinkful.com/atlanta-tech-talent-pipeline/`.

When doing that through the free domain registrar redirect tool (`name.com`),
the HTTP Referer was being lost on the trip.

We've created the app tf-attp-prod in Heroku, solely hosted up there for now,
which just takes requests and redirects them to thinkful.com, but adding the
referer domain, if any, as a param (e.g. `utm_referer=medium.com`).

As with the thinkful.com domain, the DNS servers for the ATTP.com domain is
Cloudflare and given its a Heroku app, we are using Cloudflare's "ANAME" trick,
the CNAME flattening that serves a dynamic A record for the whole domain.

Cloudflare is not used to cache any of the traffic.
