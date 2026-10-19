package subjectgen

type Catalog struct {
	Version     int         `yaml:"version" json:"version"`
	Conformance Conformance `yaml:"conformance" json:"conformance"`
	Components  []string    `yaml:"components" json:"components"`
	Routes      []Route     `yaml:"routes" json:"routes"`
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

type Output struct {
	Path    string
	Content []byte
}
