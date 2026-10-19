package subjectgen

type Catalog struct {
	Version        int                 `yaml:"version" json:"version"`
	Conformance    Conformance         `yaml:"conformance" json:"conformance"`
	Components     []string            `yaml:"components" json:"components"`
	Entities       []Entity            `yaml:"entities,omitempty" json:"entities,omitempty"`
	EntitySets     map[string][]string `yaml:"entity_sets,omitempty" json:"entity_sets,omitempty"`
	RouteFamilies  []RouteFamily       `yaml:"route_families,omitempty" json:"route_families,omitempty"`
	Routes         []Route             `yaml:"routes" json:"routes"`
	expandedRoutes []Route
}

// Entity declares one stable subject token and the protobuf message roles that
// route-family templates may reference (for example $entity or $list).
type Entity struct {
	Name     string            `yaml:"name" json:"name"`
	Messages map[string]string `yaml:"messages,omitempty" json:"messages,omitempty"`
}

type Conformance struct {
	Mode          string `yaml:"mode" json:"mode"`
	TrackingIssue string `yaml:"tracking_issue,omitempty" json:"tracking_issue,omitempty"`
}

type Route struct {
	ID            string               `yaml:"id" json:"id"`
	Pattern       string               `yaml:"pattern" json:"pattern"`
	Lifecycle     string               `yaml:"lifecycle" json:"lifecycle"`
	Conformance   Conformance          `yaml:"conformance" json:"conformance"`
	Interaction   string               `yaml:"interaction,omitempty" json:"interaction,omitempty"`
	Payload       string               `yaml:"payload,omitempty" json:"payload,omitempty"`
	Request       string               `yaml:"request,omitempty" json:"request,omitempty"`
	EmptyRequest  bool                 `yaml:"empty_request,omitempty" json:"empty_request,omitempty"`
	Replies       Replies              `yaml:"replies,omitempty" json:"replies,omitempty"`
	Parameters    map[string]Parameter `yaml:"parameters,omitempty" json:"parameters,omitempty"`
	Subscriptions []Subscription       `yaml:"subscriptions,omitempty" json:"subscriptions,omitempty"`
	Publishers    []string             `yaml:"publishers,omitempty" json:"publishers,omitempty"`
	Consumers     []string             `yaml:"consumers,omitempty" json:"consumers,omitempty"`
	Replacement   string               `yaml:"replacement,omitempty" json:"replacement,omitempty"`
	Description   string               `yaml:"description,omitempty" json:"description,omitempty"`
	parameterList []string
	familyID      string
	entityName    string
}

// RouteFamily expands one entity-parameterized route into concrete routes for
// every member of EntitySet. Message fields may refer to an entity message role
// with a $ prefix, such as $entity, $list, $create, or $update.
type RouteFamily struct {
	Route           `yaml:",inline" json:",inline"`
	EntitySet       string                   `yaml:"entity_set" json:"entity_set"`
	EntityOverrides map[string]RouteOverride `yaml:"entity_overrides,omitempty" json:"entity_overrides,omitempty"`
}

type RouteOverride struct {
	Lifecycle   string       `yaml:"lifecycle,omitempty" json:"lifecycle,omitempty"`
	Conformance *Conformance `yaml:"conformance,omitempty" json:"conformance,omitempty"`
	Publishers  []string     `yaml:"publishers,omitempty" json:"publishers,omitempty"`
	Consumers   []string     `yaml:"consumers,omitempty" json:"consumers,omitempty"`
}

type Replies struct {
	Success string `yaml:"success,omitempty" json:"success,omitempty"`
	Failure string `yaml:"failure,omitempty" json:"failure,omitempty"`
}

type Parameter struct {
	Type string `yaml:"type" json:"type"`
}

// Subscription declares a safe partial-wildcard helper. Parameters listed
// here remain concrete; every other route parameter becomes `*`.
type Subscription struct {
	Name       string   `yaml:"name" json:"name"`
	Parameters []string `yaml:"parameters,omitempty" json:"parameters,omitempty"`
}

func (r Route) ParameterList() []string {
	return append([]string(nil), r.parameterList...)
}

func (r Route) FamilyID() string {
	return r.familyID
}

func (r Route) EntityName() string {
	return r.entityName
}

func (f RouteFamily) ParameterList() []string {
	return append([]string(nil), f.parameterList...)
}

func (c Catalog) AllRoutes() []Route {
	routes := make([]Route, 0, len(c.Routes)+len(c.expandedRoutes))
	routes = append(routes, c.Routes...)
	routes = append(routes, c.expandedRoutes...)
	return routes
}

type Output struct {
	Path    string
	Content []byte
}
